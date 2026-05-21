from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import const
import ollama

def get_client():
    client = QdrantClient(path=const.DB_PATH)
    create_collection(client)
    return client
    
def create_collection(client:QdrantClient):
    collection = client.get_collection(collection_name=const.DB_NAME)
    if collection:
        return
    
    client.create_collection(collection_name=const.DB_NAME, vectors_config=VectorParams(size=768, distance=Distance.COSINE))
