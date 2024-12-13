# Web Analytics Microservice

## Overview
A simple, containerised web analytics microservice that tracks request metrics using Flask and Prometheus. This project demonstrates:
- Containerization with Docker
- Microservice architecture
- Prometheus metrics collection
- Kubernetes deployment

## Features
- Track web request counts
- Measure request latency
- Expose Prometheus metrics
- Health check endpoint

## Prerequisites
- Docker
- Kubernetes
- Python 3.9+

## Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `python app.py`

## Docker Usage
```bash
# Build the Docker image
docker build -t web-analytics:v1 .

# Run the container
docker run -p 5000:5000 -p 8000:8000 web-analytics:v1
```

## Kubernetes Deployment
```bash
# Apply the Kubernetes deployment
kubectl apply -f k8s-deployment.yaml
```
