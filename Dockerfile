# Use the official Python image from Docker Hub
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/code

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy the requirements.txt file into the container
COPY requirements.txt /code/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /code/

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run the Django server
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
