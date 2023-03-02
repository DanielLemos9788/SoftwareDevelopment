# Base image
FROM python:3.9
ENV PYTHONUNBUFFERED=1
# Set work directory
WORKDIR /app
# Copy requirements file
COPY requirements.txt .
# Install requirements
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . .


