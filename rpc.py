import grpc
import flow.access.access_pb2_grpc as access_pb2_grpc
import flow.access.access_pb2 as access_pb2


MAIN_NODE = 'access.mainnet.nodes.onflow.org:9000'


def main():
    channel = grpc.insecure_channel(MAIN_NODE)
    stub = access_pb2_grpc.AccessAPIStub(channel)
    
    response = stub.GetLatestBlock(access_pb2.GetLatestBlockRequest())
    latest_block_heght = response.block.height

    response = stub.GetEventsForHeightRange(access_pb2.GetEventsForHeightRangeRequest(
        type='A.c1e4f4f4c4257510.Market.MomentPurchased',
        start_height=latest_block_heght - 100,
        end_height=latest_block_heght))

    print(response)


if __name__ == '__main__':
    main()
