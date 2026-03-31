# Use a lightweight Python base
FROM python:3.11-slim

# Install 'uv' from the official binary to keep things fast
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Copy only the dependency file first (Docker caching optimization)
COPY requirements.txt .

# Install dependencies system-wide using uv
RUN uv pip install --system --no-cache -r requirements.txt

# Copy the rest of your code
COPY ingest_flight_data.py .

CMD ["python", "ingest_flight_data.py"]