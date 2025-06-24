# Use official Python image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy all files into container
COPY . .

# Install Flask
RUN pip install Flask

# Expose port 5000
EXPOSE 5000

# Run your app
CMD ["python", "app.py"]
