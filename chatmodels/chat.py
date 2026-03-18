from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(model="groq/compound-mini")

#to invoke model we use model.invoke method
#and then we should save that response

response = model.invoke("Hello")


# print(response) we have to only take content from the answer

print(response.content)



# from dotenv import load_dotenv

# load_dotenv()

# from langchain_groq import ChatGroq

# model = ChatGroq(model="groq/compound-mini")

# #to invoke model we use model.invoke method
# #and then we should save that response

# response = model.invoke("What is Rag")


# # print(response) we have to only take content from the answer

# print(response.content)

