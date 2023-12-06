import pika

connection_params = pika.ConnectionParameters(
    host='rabbitmq',
    credentials=pika.PlainCredentials(
        username='myuser',
        password='mypassword'
    ),
)

def callback(ch, method, properties, body):
    print(f" [x] Received: {body}")

def consume_messages():
    try:
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()

        # Declare a fanout exchange named 'logs'
        channel.exchange_declare(exchange='logs', exchange_type='fanout')

        # Declare a queue with a random name (exclusive=True creates a temporary queue)
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        # Bind the queue to the 'logs' exchange
        channel.queue_bind(exchange='logs', queue=queue_name)

        print(' [*] Waiting for messages. To exit, press CTRL+C')

        # Set up the consumer with the callback function
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Start consuming messages
        channel.start_consuming()
    except Exception as e:
        print(f"Consuming message failed: {e}")


if __name__ == '__main__':
    print("consumer started")
    while True:
        consume_messages()
