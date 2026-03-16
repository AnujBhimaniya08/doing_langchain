from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
documents = [
    "delhi is the capital of India",
    "my name is khan",
    "im the best"
]
result = embedding.embed_documents(documents)
print(str(result))