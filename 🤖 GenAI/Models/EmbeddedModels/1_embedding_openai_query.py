from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=16)

result = embedding.embed_query("My name is Ajay")

print(str(result))

