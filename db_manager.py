from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from llm_manager import embed
import const


def get_client():
    client = QdrantClient(path=const.DB_PATH)
    create_collection(client)
    return client


def create_collection(client: QdrantClient):
    if client.collection_exists(collection_name=const.DB_NAME):
        return
    client.create_collection(
        collection_name=const.DB_NAME,
        vectors_config=VectorParams(
            size=const.EMBED_DIMENSIONS, distance=Distance.COSINE
        ),
    )


def insert_data(data, message_id):
    vect = embed(data)[0]
    client = get_client()
    client.upsert(
        collection_name=const.DB_NAME,
        wait=False,
        points=[PointStruct(id=message_id, vector=vect, payload={"data": data})],
    )
    client.close()

def load_data(pattern):
    vect = embed(pattern)[0]
    client = get_client()
    memories = []

    for point in client.query_points(
        collection_name=const.DB_NAME, query=vect, limit=10
    ).points:
        memories.append(point.payload["data"])

    client.close()
    return memories
