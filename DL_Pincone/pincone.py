import pinecone
from pinecone import ServerlessSpec

# Initialize Pinecone
pinecone.init(api_key='02f59ba4-d50d-4684-bdd9-d1a2b5e431ca')

# Define index name
INDEX_NAME = 'my-semantic-search-index'

# Check if the index already exists and delete it if it does
if INDEX_NAME in pinecone.list_indexes():
    pinecone.delete_index(INDEX_NAME)

# Create a new index
pinecone.create_index(
    name=INDEX_NAME,
    dimension=1536,  # Specify the dimension of the embeddings
    metric='cosine',  # Similarity metric
    spec=ServerlessSpec(cloud='aws', region='us-west-2')  # Serverless spec with AWS and region
)

# Initialize the index object
index = pinecone.Index(INDEX_NAME)

# Optionally, print index details to verify
print(index.describe_index_stats())
