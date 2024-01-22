import pika

# Replace 'guest' and 'guest' with your RabbitMQ username and password
credentials = pika.PlainCredentials(username='admin', password='admin')
# Replace '/' with your actual virtual host if it's different
virtual_host = 'rabbithost'  

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials, virtual_host=virtual_host))
channel = connection.channel()

# Declare an exchange named 'logs' of type 'fanout' (broadcasts messages to all queues)
channel.exchange_declare(exchange='logs', exchange_type='fanout')
######## subscriber

# channel.queue_bind(queue='my_queue1')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# # Create a new anonymous queue exclusive to this subscriber
# result = channel.queue_declare(queue='my_queue1', exclusive=True)
# queue_name = result.method.queue

# Bind the queue to the 'logs' exchange
channel.queue_bind(queue='my_queue1', exchange='logs')

print(' [*] Waiting for messages. To exit, press Ctrl+C')

# Set up the callback function to handle incoming messages
channel.basic_consume(queue='my_queue1', on_message_callback=callback, auto_ack=True)

# Start consuming messages
channel.start_consuming()
