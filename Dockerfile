# Use an official Python runtime as a Parent Image
FROM python:3.11.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirement.txt

# Install the uvicorn[standard] package. Getting error while using it in the requirement.txt
RUN pip install "uvicorn[standard]"

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]