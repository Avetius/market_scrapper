# publish_to_rabbitmq.py
import os
import sys
import pika

# Access environmental variables
messageBrokerHost = os.getenv("MB_HOST")

# Use the variables as needed
print(f"GATE_HOST: {messageBrokerHost}")

def publishMessage(result, exchange='', routing_key=''): # , queue=''
    connection = pika.BlockingConnection(pika.ConnectionParameters(messageBrokerHost))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='fanout')
    channel.queue_declare(queue=routing_key)
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=result)
    print(f"Message was sent to Exchange > '{exchange}', Queue > '{queue}', Routing Key > '{routing_key}'")
    connection.close()


def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")


def receive_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='result_queue')
    channel.basic_consume(queue='result_queue', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


def close_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    connection.close()

