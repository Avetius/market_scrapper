# publish_to_rabbitmq.py
# import os
# import sys
import pika
# from dotenv import load_dotenv

# load_dotenv()
# Access environmental variables
RABBITMQ_URL = 'rabbitmq'# = os.getenv("RABBITMQ_URL")

# Use the variables as needed
print(f"RABBITMQ_URL: {RABBITMQ_URL}")

# def publishMessage(message, exchange='', routing_key=''): # , queue=''
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_URL))
#     print(">>>>>>>>>>>>>>     connection     <<<<<<<<<<<<<<<<<<")
#     channel = connection.channel()
#     print(">>>>>>>>>>>>>>     Channel     <<<<<<<<<<<<<<<<<<")
#     channel.exchange_declare(exchange=exchange, exchange_type='fanout')
#     channel.queue_declare(queue=routing_key)
#     print(">>>>>>>>>>>>>>     Q U E U E     <<<<<<<<<<<<<<<<<<")
#     channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
#     print(f"Message was sent to Exchange > '{exchange}', Queue > '{routing_key}', Routing Key > '{routing_key}'")
#     connection.close()

connection_params = pika.ConnectionParameters(
    host='rabbitmq',
    # connection_attempts=18,
    # retry_delay=5
    # port=5672,
    credentials=pika.PlainCredentials(
        username='myuser',
        password='mypassword'
    ),
)


def publish(message, routing_key='', exchange=''):
    # RabbitMQ server connection parameters
    conn
    try:
        connection = pika.BlockingConnection(connection_params)
        print("connection ok")
        channel = connection.channel()
        print("channel ok")
        channel.exchange_declare(exchange=exchange, exchange_type='fanout')
        print("exchange ok")
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
        print(f" [x] Sent {message}")
        conn = connection
        # connection.close()
        # attempts = -1
        return conn
    except Exception as e:
        print(f"Sending message failed: {e}")


def callback(ch, method, properties, body):
    print(f" [x] {body}")


def receiveMessages(queue='', exchange=''):
    try:
        connection = pika.BlockingConnection(connection_params)
        print("connection ok")
        channel = connection.channel()
        print("channel ok")
        channel.exchange_declare(exchange=exchange, exchange_type='fanout')
        print("exchange ok")
        channel.queue_declare(queue=queue)
        print("queue_declare")
        # queue_name = result.method.queue
        # print(f"queue_name >>>>>>>>>>> {queue_name}")
        channel.queue_bind(exchange=exchange, queue=queue)
        print("queue_bind")
        channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        print("Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
    except Exception as e:
        print(f"Failed recieve message: {e}")

# def close_connection():
#     connection = pika.BlockingConnection(connection_params)
#     connection.close()
