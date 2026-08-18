from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-4.1')

result = model.invoke('What is the capital of India')

print(result.content)



#print(result.content)




#"ChatOpenAI returns an AIMessage object containing both response text and execution metadata, not just plain output."


# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# load_dotenv()

# model = ChatOpenAI(model='gpt-4',temperature=1.5, max_completion_tokens=100)

# # result = model.invoke('suggest me 5 indian female names')
# result = model.invoke('write 5 line poem on AI hipe')


# print(result.content)