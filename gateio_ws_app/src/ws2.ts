import WebSocket from 'ws';
import * as amqp from 'amqplib';
import { InfluxDB } from 'influx';
import dotenv from 'dotenv';

dotenv.config();

const webSocketUrl = process.env.TEST_WS_URL || '';
const apiKey = process.env.API_KEY || '';
const apiSecret = process.env.API_SECRET || '';
const rabbitMQUrl = 'YOUR_RABBITMQ_URL';
const influxDBUrl = 'YOUR_INFLUXDB_URL'; // Replace with your InfluxDB connection URL
const influxDBDatabase = 'your_database_name'; // Replace with your InfluxDB database name
const channelsToSubscribe = ['spot.tickers', 'spot.trades'];

// Initialize InfluxDB client
const influx = new InfluxDB({
  host: influxDBUrl,
  database: influxDBDatabase,
});

async function connectWebSocket() {
  console.log('webSocketUrl > ', webSocketUrl);
  console.log('apiKey > ', apiKey);
  console.log('apiSecret > ', apiSecret);
  const socket = new WebSocket(webSocketUrl);

  socket.on('open', () => {
    console.log('WebSocket connected');

    const authMessage = JSON.stringify({ action: 'authenticate', key: apiKey, secret: apiSecret });
    socket.send(authMessage);
    // Subscribe to channels after connecting
    channelsToSubscribe.forEach(channel => {
      socket.send(JSON.stringify({ action: 'subscribe', channel }));
    });
  });

  socket.on('message', (data: WebSocket.Data) => {
    try {
      const message = JSON.parse(data.toString());
      console.log('message > ', message);
      // handleWebSocketMessage(message);                   // <<<<<<<<<<<
    } catch (error) {
      console.error('Error parsing WebSocket message:', error);
    }
  });

  socket.on('close', () => {
    console.log('WebSocket connection closed');
  });

  socket.on('error', (error) => {
    console.error('WebSocket error:', error);
  });
}

async function handleWebSocketMessage(message: any) {
  // Handle WebSocket message
  console.log('Received WebSocket message:', message);
  const rabbitMQMessage = JSON.stringify(message);
  // publishToRabbitMQ(rabbitMQMessage);                       // <<<<<<<<<<<
  // Save the data to InfluxDB
  saveToInfluxDB(message);
}

async function saveToInfluxDB(data: any) {
  try {
    // Define InfluxDB measurement and fields based on your data structure
    // const measurement = 'your_measurement_name';
    // const fields = {
    //   field1: data.field1,
    //   field2: data.field2,
    //   // Add more fields as needed
    // };

    // // Create a new InfluxDB point
    // const point = new Point(measurement).fields(fields);

    // // Write the point to InfluxDB
    // await influx.writePoints([point]);
    // console.log('Data saved to InfluxDB');
  } catch (error) {
    console.error('Error saving data to InfluxDB:', error);
  }
}

async function publishToRabbitMQ(message: string) {
  try {
    const connection = await amqp.connect(rabbitMQUrl);
    const channel = await connection.createChannel();

    const exchange = 'your_exchange_name';
    const routingKey = 'your_routing_key';

    // Ensure the exchange exists
    await channel.assertExchange(exchange, 'fanout', { durable: false });

    // Publish the message to the exchange
    channel.publish(exchange, routingKey, Buffer.from(message));
    console.log('Message published to RabbitMQ');

    // Close the channel and connection
    await channel.close();
    await connection.close();
  } catch (error) {
    console.error('Error publishing to RabbitMQ:', error);
  }
}
// Connect to WebSocket and start listening for messages
connectWebSocket();