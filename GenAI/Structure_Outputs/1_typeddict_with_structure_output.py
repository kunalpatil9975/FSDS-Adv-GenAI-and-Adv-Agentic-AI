from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI(model="gpt-4.1")


#schema
class Review(TypedDict):

    summary: Annotated [str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]

structured_model = model.with_structured_output(Review)

#result = structured_model.invoke("""The hardware is great, but the software feels bloated.
#There are too many pre-installed apps that I can't remove. Also, the UI looks outdated
#compared to other brands. Hoping for a software update to fix this.""")

result = structured_model.invoke("""The phone is extremely disappointing. The battery drains very quickly,
the device heats up during normal use, and the software is full of bugs. Apps crash frequently and the user
interface feels slow and outdated. I regret buying this product and would not recommend it to anyone.""")

#result = structured_model.invoke("""This phone is fantastic. The performance is smooth, the battery easily lasts all day,
#and the camera quality is excellent. The design feels premium and the software experience is fast and clean. 
#I am very happy with this purchase and would highly recommend it.""")

print(result)
print(result['summary'])
print(result['sentiment'])