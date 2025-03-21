# deployment/Dockerfile
# Stage 1: Builder
FROM python:3.9-slim AS builder

WORKDIR /app
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends libgomp1 && \
    rm -rf /var/lib/apt/lists/*

COPY src/ ./src/
COPY data/ ./data/
COPY models/ ./models/

ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000

CMD ["gunicorn", "src.app:app", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120"]