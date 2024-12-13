from flask import Flask, request
from prometheus_client import start_http_server, Counter, Gauge
import random
import time

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('web_analytics_request_total', 'Total Web Request Count', ['method', 'endpoint'])
REQUEST_LATENCY = Gauge('web_analytics_request_latency_seconds', 'Request latency', ['method', 'endpoint'])

@app.route('/analytics', methods=['POST'])
def track_analytics():
    start = time.time()
    
    # Simulate processing analytics data
    data = request.get_json()
    
    # Record metrics
    REQUEST_COUNT.labels(method=request.method, endpoint='/analytics').inc()
    
    # Simulate some processing time
    time.sleep(random.uniform(0.1, 0.5))
    
    REQUEST_LATENCY.labels(method=request.method, endpoint='/analytics').set(time.time() - start)
    
    return {'status': 'success', 'message': 'Analytics tracked'}

@app.route('/health', methods=['GET'])
def health_check():
    REQUEST_COUNT.labels(method=request.method, endpoint='/health').inc()
    return {'status': 'healthy'}

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
