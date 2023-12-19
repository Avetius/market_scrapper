import redis
import asyncio


def callback(message):
    print(f" [x] data: {message['data']} channel: {message['channel']}")


def subscribe_channel(channel):
    try:
        # Connect to the local Redis server
        r = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

        # Create a new pubsub instance and subscribe to the specified channel
        pubsub = r.pubsub()
        pubsub.subscribe(channel)

        print(f' [*] Subscribed to channel: {channel}. Waiting for messages.')

        # Start listening for messages
        for message in pubsub.listen():
            if message['type'] == 'message':
                callback(message)

    except Exception as e:
        print(f"Getting message failed: {e}")


def publish_message(channel, message):
    try:
        # Connect to the local Redis server
        r = redis.StrictRedis(host='redis', port=6379, decode_responses=True)
        # Publish the message to the specified channel
        r.publish(channel, message)
        # print(f" [x] Sent: {message} to channel: {channel}")
        print(f" [x] Sent: message to channel: {channel}")
        return 0
    except Exception as e:
        print(f"Sending message failed: {e}")
        return 1
    # return 1


async def wait_for_redis(host='redis', port=6379, timeout=10):
    attempts = 0
    while True:
        try:
            # time.sleep(1)
            # Attempt to connect to Redis
            connection = redis.StrictRedis(host=host, port=port, decode_responses=True)
            connection.ping()
            # If connection succeeds, break out of the loop
            break
        except redis.ConnectionError as e:
            # Handle the connection error if needed
            print(f"Error connecting to Redis: {e}")

        await asyncio.sleep(1)
        attempts=attempts+1
        # Check if the timeout has been reached
        if attempts > 60:
            raise TimeoutError("Timeout waiting for Redis to become available")


# Example usage:
# if __name__ == '__main__':
#     try:
#         wait_for_redis()
#         print("Redis is available sub2!")
#         channel_to_subscribe = 'example_channel'
#         channel_to_publish = 'example_channel'
#         subscribe_channel(channel_to_subscribe)
#         timestamp = str(int(time.time()))
#         # redis_client.zadd(key, {value: timestamp})
#         message_to_send = timestamp + " Hello, Redis Pub/Sub!"
#         publish_message(channel_to_publish, str(message_to_send))
        
#     except TimeoutError as e:
#         print(f"Error: {e}")
#         # Handle the timeout error
