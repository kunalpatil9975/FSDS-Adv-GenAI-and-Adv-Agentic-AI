from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model = 'sentence-transformers/all-MiniLM-L6-v2')

#text = "Delhi is the capital of India"
documents =  [
    "Delhi is the capital of India",
    "Mumbai is the capital of Maharashtra",
    "Paris is the capital of France"

]

#vector = embedding.embed_query(text)
vector = embedding.embed_documents(documents)
print(str(vector))