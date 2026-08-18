#from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Attention_all_you_need1.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

#print(result[50])

print(result[50].page_content)