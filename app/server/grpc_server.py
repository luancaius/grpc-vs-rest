import grpc
from concurrent import futures
import time
import logging
from app.proto import service_pb2
from app.proto import service_pb2_grpc

class DataTransferServicer(service_pb2_grpc.DataTransferServiceServicer):
    def UploadData(self, request, context):
        start_time = time.time()
        payload = request.payload
        size = len(payload)
        
        duration = time.time() - start_time
        # logger.info(f"gRPC Request processed in {duration:.4f}s, size: {size}")

        return service_pb2.DataResponse(
            success=True,
            message="Data received via gRPC",
            received_size=size
        )

def start_grpc_server(port=50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_DataTransferServiceServicer_to_server(DataTransferServicer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"gRPC server started on port {port}")
    server.wait_for_termination()

