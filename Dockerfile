FROM python:3.10-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy everything
COPY . .

EXPOSE 5000

# Run Flask app from correct path
CMD ["python", "app/api/app.py"]

