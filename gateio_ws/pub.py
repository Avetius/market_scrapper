import pika

rabbit_params = {
    "username": "admin",
    "password": "admin",
    "host": "localhost",
    "virtual_host": "rabbithost",
    "exchange": "logs",
    "queue_name": "my_queue1",
}

# Replace 'guest' and 'guest' with your RabbitMQ username and password
credentials = pika.PlainCredentials(username='admin', password='admin')
# Replace '/' with your actual virtual host if it's different
virtual_host = 'rabbithost'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials, virtual_host=virtual_host))
channel = connection.channel()

# Declare an exchange named 'logs' of type 'fanout' (broadcasts messages to all queues)
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Declare a durable queue named 'my_queue'
queue_name = 'my_queue1'
channel.queue_declare(queue=queue_name, durable=True)

# publisher
message = 'BOLYOLYOLYOLYOLYO!'
channel.basic_publish(exchange='logs', routing_key=queue_name, body=message)

print(f" [x] Sent '{message}'")

connection.close()
