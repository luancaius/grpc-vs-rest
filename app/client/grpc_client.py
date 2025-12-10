import grpc
import time
from app.proto import service_pb2
from app.proto import service_pb2_grpc
from app.common.metrics import Instrumentor

class GrpcClient:
    def __init__(self, host="localhost", port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = service_pb2_grpc.DataTransferServiceStub(self.channel)
        self.instrumentor = Instrumentor()

    def send_data(self, payload):
        start_time = time.time()
        try:
            request = service_pb2.DataRequest(
                payload=payload,
                timestamp=int(time.time())
            )
            response = self.stub.UploadData(request)
            self.instrumentor.record(start_time)
            return response
        except grpc.RpcError as e:
            print(f"gRPC Error: {e}")
            return None

    def get_metrics(self):
        return self.instrumentor.metrics.get_summary()

