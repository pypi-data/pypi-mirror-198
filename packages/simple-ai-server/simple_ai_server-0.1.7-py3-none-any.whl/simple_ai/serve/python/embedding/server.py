"""The Python implementation of the gRPC server."""

from concurrent import futures
import logging

import grpc
from . import llm_embed_pb2
from . import llm_embed_pb2_grpc

from .model import LanguageModel


class LanguageModelServicer(llm_embed_pb2_grpc.LanguageModelServicer):
    """Provides methods that implement functionality of route guide server."""
    
    def __init__(self, model=LanguageModel()) -> None:
        super().__init__()
        self.model = model
    
    def Embed(self, request, context):
        predicted = self.model.embed(
            inputs=request.inputs,
        )
        return llm_embed_pb2.ListOfEmbeddings(reply=predicted)


def serve(address='[::]:50051', model_servicer=LanguageModelServicer()):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    llm_embed_pb2_grpc.add_LanguageModelServicer_to_server(
        model_servicer, server)
    server.add_insecure_port(address=address)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    import argparse
    
    logging.basicConfig()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('address', type=str, default='[::]:50051')
    args = parser.parse_args()

    serve(address=args.address)
