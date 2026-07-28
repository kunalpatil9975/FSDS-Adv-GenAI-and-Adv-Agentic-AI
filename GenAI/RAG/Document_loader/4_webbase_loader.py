from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()


url = 'https://www.amazon.in/Apple-MacBook-15-inch-10-core-Unified/dp/B0DZDDK21R/ref=sr_1_1_sspa?crid=TF34Z5ANXYA6&dib=eyJ2IjoiMSJ9.vZqyvdLD37T0s0qPp8_ABmn9z0LOEgHiNn7ngoqNE3HMpaiZWQoXmxCUPLAcj4dtpowLMrsaRY0bjQuWowy3yv531Au-1hzmujbyhR4as2PdUnsSppSHcmjtXv4SaYsb9iNNvPPIkEm3dIVjvQKEhKQBeWabL3ziyalAzEvNY6YuhRdruMibk2X7Lls3T7JYEfACn4XP-S5sSYy8q7EuyoL350qlWduK_MRtWTygu7A.MQ0EW0edCILOlzssygL8zPsYo9xF21iE_7D5zYMStL0&dib_tag=se&keywords=macbook%2Bair%2Bm4&qid=1773038751&sprefix=mac%2Caps%2C360&sr=8-1-spons&aref=TiCOXqXXof&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))