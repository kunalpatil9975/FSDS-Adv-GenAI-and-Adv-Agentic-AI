from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

#llm = [OpenAI,gpt-3.5,invote]
# Object = data,logic,action}
result = llm.invoke('What is the capital of India')

print(result)




# llm is:

# An LLM wrapper object
# Provides a standard interface to interact with the underlying model
# Internally handles:
# API calls
# Authentication (via .env)
# Request/response formatting


# Your input → "What is the capital of India"
# llm.invoke() → sends request to OpenAI API
# Model processes input
# Returns response → "New Delhi"