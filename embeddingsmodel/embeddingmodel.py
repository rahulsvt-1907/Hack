from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(

    model="text-embedding-3-small"
)

text = [
    "hello how are you?",

    "howww are you?",
   "i am fine",

    "i am good",

    "i am bad",

    "i am good",
]
vector = embeddings.embed_documents(text)

print(vector)

