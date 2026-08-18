from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

# HuggingFacePipeline → loads a model from Hugging Face and runs it locally
# ChatHuggingFace → converts that model into a chat-style model (Human ↔ AI conversation)

#Load the Model (LLM)

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    #pipeline_kwargs=dict(max_new_tokens=100, temperature=0.7)

)

#C:\Users\ajayc\.cache\huggingface\hub\

#Convert into Chat Model, “Convert text generator into conversational AI”

model = ChatHuggingFace(llm=llm)

result = model.invoke('What is the capital of India')
print(result.content)