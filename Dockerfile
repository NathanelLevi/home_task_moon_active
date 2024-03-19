# Use Python base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Command to run when the container starts
CMD ["python", "app.py"]