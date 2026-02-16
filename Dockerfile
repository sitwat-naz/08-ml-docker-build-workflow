# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run preprocessing and training (optional for CI)
CMD ["python", "src/train.py"]
