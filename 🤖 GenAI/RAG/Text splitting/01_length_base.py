#from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """“Attention Is All You Need” introduced a new paradigm for processing sequential data by replacing recurrence and 
convolution with attention mechanisms. The Transformer architecture enables models to examine all elements of a sequence 
simultaneously and determine which parts are most relevant to each other. By combining self-attention, multi-head attention, 
positional encoding, and feed-forward neural networks, the Transformer provides a powerful framework for understanding complex 
relationships in data. This design not only improved performance on language tasks but also enabled the development of the 
large-scale generative AI systems that are widely used today. The paper’s central insight—that attention alone can model
 relationships within sequences—has reshaped modern AI research and continues to influence the development of new models and 
 applications across many fields.
"""





splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)