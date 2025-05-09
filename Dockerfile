# Use official Python 3.10 image
FROM python:3.10-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt  # This is now at /app, which has setup.py

# Change to src before running
WORKDIR /app/src

# Expose port
EXPOSE 8080

# Run the FastAPI app
CMD ["uvicorn", "text_classifier.main:app", "--host", "0.0.0.0", "--port", "8080"]
