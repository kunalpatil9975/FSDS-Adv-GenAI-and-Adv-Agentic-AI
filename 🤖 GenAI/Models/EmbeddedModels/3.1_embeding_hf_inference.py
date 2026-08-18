from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()



embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
)

documents = [
    "Delhi is the capital of India",
    "Mumbai is the capital of Maharashtra",
    "Paris is the capital of France"
]

vectors = embedding.embed_documents(documents)

print(vectors)
print("No. of documents:", len(vectors))
print("Dimension of first vector:", len(vectors[0]))