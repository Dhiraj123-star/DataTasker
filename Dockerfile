# Stage 1: Build stage with full Python and build tools
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies (if you need any compiling packages, add here)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install to a temporary directory (will be copied later)
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Copy application code
COPY . .

# Stage 2: Final minimal image
FROM python:3.11-slim

WORKDIR /app

# Copy only the installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy app source code from builder stage
COPY --from=builder /app /app

# Expose FastAPI port
EXPOSE 8000

# Command to run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
