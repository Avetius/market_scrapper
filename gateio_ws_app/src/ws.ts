import WebSocket from 'ws';
import * as amqp from 'amqplib';

const ws = new WebSocket('ws://localhost:8080');

let amqpConn: amqp.Connection;

async function connectRabbitMQ() {
  amqpConn = await amqp.connect('amqp://localhost');
}

ws.on('open', () => {
  ws.send(JSON.stringify({subscribe: 'channel1'}));
  ws.send(JSON.stringify({subscribe: 'channel2'})); 
});

ws.on('message', async (data: string) => {
  const msg = JSON.parse(data);
  
  if(!amqpConn) {
    await connectRabbitMQ(); 
  }

  const channel = await amqpConn.createChannel();  

  await channel.assertQueue('channel1');
  await channel.assertQueue('channel2');

  if(msg.channel === 'channel1') {
    channel.sendToQueue('channel1', Buffer.from(JSON.stringify(msg))); 
  }

  if(msg.channel === 'channel2') {
    channel.sendToQueue('channel2', Buffer.from(JSON.stringify(msg)));
  }

});