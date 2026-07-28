from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy as np

load_dotenv()

from sklearn.metrics.pairwise import cosine_similarity

embedding = OpenAIEmbeddings(model = 'text-embedding-3-small', dimensions=30)

document = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]



#query = 'Tell me about virat kohli'
query = 'Tell me about Jasprit Bumrah'

document_embedding = embedding.embed_documents(document)

print(str(document_embedding))

print("********************************************")

query_embedding = embedding.embed_query(query)

print(str(query_embedding))
print("********************************************")

print(cosine_similarity([query_embedding],document_embedding))

print("********************************************")


# score =  cosine_similarity([query_embedding], document_embedding)[0]

# print(list(enumerate(score)))
# print( sorted(list(enumerate(score)),key=lambda x:x[1]))

# index, score = sorted = sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

# print("*******************************************")

# print(query)
# print(document[index])
# print("Similarity score is :", score)
