import argparse
import time
import random
import string
from app.client.rest_client import RestClient
from app.client.grpc_client import GrpcClient

def generate_payload(size_bytes):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size_bytes))

def run_benchmark(client, payload, iterations):
    print(f"Running {iterations} iterations...")
    for _ in range(iterations):
        client.send_data(payload)
    
    metrics = client.get_metrics()
    print("\nBenchmark Results:")
    print("-" * 20)
    for key, value in metrics.items():
        if "duration" in key:
            print(f"{key}: {value:.6f}s")
        else:
            print(f"{key}: {value}")
    print("-" * 20)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark Client")
    parser.add_argument("--type", choices=["rest", "grpc"], required=True, help="Transport type")
    parser.add_argument("--size", type=int, default=1024, help="Payload size in bytes")
    parser.add_argument("--iterations", type=int, default=100, help="Number of requests")
    
    args = parser.parse_args()

    payload = generate_payload(args.size)
    print(f"Generated payload of size: {len(payload)} bytes")

    if args.type == "rest":
        client = RestClient()
        print("Using REST Client")
    else:
        client = GrpcClient()
        print("Using gRPC Client")

    run_benchmark(client, payload, args.iterations)

