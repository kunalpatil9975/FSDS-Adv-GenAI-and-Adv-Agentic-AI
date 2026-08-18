from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI()

st.header('Reasearch Tool')

user_input = st.text_input("Enter your prompt")



if st.button('Summarize'):
    
    result = model.invoke(user_input)
    st.write(result.content)




#streamlit run .\Prompts\prompts_ui.py
# pip install -r "C:\Users\ajayc\Desktop\Langchain\requirements.txt.txt"