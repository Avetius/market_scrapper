# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your cron file to the cron.d directory
COPY your-cron /etc/cron.d/your-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/your-cron

# Apply cron job
RUN crontab /etc/cron.d/your-cron

# Run the command on container startup
CMD ["cron", "-f"]