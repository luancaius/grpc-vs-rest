import argparse
import multiprocessing
from app.server.rest_server import start_rest_server
from app.server.grpc_server import start_grpc_server

def run_rest():
    print("Starting REST Server...")
    start_rest_server()

def run_grpc():
    print("Starting gRPC Server...")
    start_grpc_server()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start Servers")
    parser.add_argument("--type", choices=["rest", "grpc", "both"], default="both", help="Server type to run")
    args = parser.parse_args()

    processes = []

    if args.type in ["rest", "both"]:
        p_rest = multiprocessing.Process(target=run_rest)
        p_rest.start()
        processes.append(p_rest)

    if args.type in ["grpc", "both"]:
        p_grpc = multiprocessing.Process(target=run_grpc)
        p_grpc.start()
        processes.append(p_grpc)

    for p in processes:
        p.join()

