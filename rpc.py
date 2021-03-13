import grpc
import flow.access.access_pb2_grpc as access_pb2_grpc
import flow.access.access_pb2 as access_pb2


MAIN_NODE = 'access.mainnet.nodes.onflow.org:9000'


def main():
    channel = grpc.insecure_channel(MAIN_NODE)
    stub = access_pb2_grpc.AccessAPIStub(channel)
    response = stub.GetLatestBlock(access_pb2.GetLatestBlockRequest())
    print(response.block.height)


if __name__ == '__main__':
    main()
