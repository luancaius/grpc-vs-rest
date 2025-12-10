import requests
import json
import time
from app.common.metrics import Instrumentor

class RestClient:
    def __init__(self, host="localhost", port=5001):
        self.url = f"http://{host}:{port}/upload"
        self.instrumentor = Instrumentor()

    def send_data(self, payload):
        start_time = time.time()
        try:
            response = requests.post(self.url, json={
                "payload": payload,
                "timestamp": int(time.time())
            })
            response.raise_for_status()
            self.instrumentor.record(start_time)
            return response.json()
        except Exception as e:
            print(f"REST Error: {e}")
            return None

    def get_metrics(self):
        return self.instrumentor.metrics.get_summary()

