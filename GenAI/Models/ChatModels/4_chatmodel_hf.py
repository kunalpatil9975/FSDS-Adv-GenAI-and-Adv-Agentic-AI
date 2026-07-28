from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

#llm = HuggingFaceEndpoint(repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0', task='text-generation')

#Load the Model (LLM)

llm = HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-8B-Instruct", task="text-generation")

#Convert into Chat Model, “Convert text generator into conversational AI”

model = ChatHuggingFace(llm=llm)

ChatHuggingFace(llm)

result = model.invoke('What is the capital of India')

print(result.content)


#HuggingFace models return raw generation text, while LangChain does minimal abstraction here. Unlike OpenAI, we must handle formatting ourselves.”