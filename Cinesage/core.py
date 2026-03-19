from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplates


model=ChatMistralAI(model='mistral-small-2506')

response=model.invoke("hello,explain me what is GAN?")


print(response.content)
#we should use template prompt as its more handy and understandable

