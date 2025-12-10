from flask import Flask, request, jsonify
import time
import logging

app = Flask(__name__)
logger = logging.getLogger("RestServer")

@app.route('/upload', methods=['POST'])
def upload():
    start_time = time.time()
    data = request.json
    payload = data.get('payload', '')
    timestamp = data.get('timestamp')
    
    # Process "data" (simulated)
    size = len(payload)
    
    duration = time.time() - start_time
    # In a real scenario, we might log metrics here or push to a collector
    # logger.info(f"REST Request processed in {duration:.4f}s, size: {size}")

    return jsonify({
        "success": True, 
        "message": "Data received via REST", 
        "received_size": size
    })

def start_rest_server(port=5001):
    app.run(port=port, debug=False)

