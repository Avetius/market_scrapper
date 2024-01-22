######## setup
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare an exchange named 'logs' of type 'fanout' (broadcasts messages to all queues)
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# publisher
message = 'Hello, RabbitMQ!'
channel.basic_publish(exchange='logs', routing_key='', body=message)

print(f" [x] Sent '{message}'")

connection.close()

######## subscriber

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Create a new anonymous queue exclusive to this subscriber
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind the queue to the 'logs' exchange
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for messages. To exit, press Ctrl+C')

# Set up the callback function to handle incoming messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Start consuming messages
channel.start_consuming()
