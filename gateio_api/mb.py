# publish_to_rabbitmq.py
import os
import sys
import pika
from dotenv import load_dotenv

load_dotenv()
# Access environmental variables
RABBITMQ_URL = os.getenv("RABBITMQ_URL")

# Use the variables as needed
print(f"RABBITMQ_URL: {RABBITMQ_URL}")

def publishMessage(result, exchange='', routing_key=''): # , queue=''
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='fanout')
    channel.queue_declare(queue=routing_key)
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=result)
    print(f"Message was sent to Exchange > '{exchange}', Queue > '{routing_key}', Routing Key > '{routing_key}'")
    connection.close()


def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")


def receiveMessages(queue='result_queue'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


def close_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_URL))
    connection.close()

