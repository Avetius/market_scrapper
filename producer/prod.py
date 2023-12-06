import pika

connection_params = pika.ConnectionParameters(
    host='rabbitmq',
    credentials=pika.PlainCredentials(
        username='myuser',
        password='mypassword'
    ),
)

def publish_message(message):
    try:
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()

        # Declare a fanout exchange named 'logs'
        channel.exchange_declare(exchange='logs', exchange_type='fanout')

        # Publish the message to the 'logs' exchange
        channel.basic_publish(exchange='logs', routing_key='', body=message)

        print(f" [x] Sent: {message}")

        connection.close()
    except Exception as e:
        print(f"Sending message failed: {e}")


if __name__ == '__main__':
    message_to_send = "Hello, RabbitMQ!"
    while True:
        publish_message(message_to_send)