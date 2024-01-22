#!/bin/bash

# Wait for RabbitMQ to be ready
sleep 10

# RabbitMQ commands to create a virtual host and set permissions
rabbitmqctl add_vhost admin
rabbitmqctl set_permissions -p myvhost admin ".*" ".*" ".*"