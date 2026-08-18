from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatOpenAI()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser() #The best use case for this parser is when you want to extract a specific part of the output. For example, if you want to extract a summary from a longer text, you can use the StrOutputParser to extract just the summary.
#The best use of parsers is when you use chains. For example, you can use the StrOutputParser to extract the summary from the output of the first prompt, and then use that summary as input for the second prompt. This way, you can create a chain of prompts and parsers that work together to produce a final output.

chain = template1 | model | parser | template2 | model | parser



#chain is nothing but putting all your steps into pipeline fashion to make it single workflow

result = chain.invoke({'topic':'black hole'})

print(result)


#Model,Prompt,Structure output,Output parser,Chain.