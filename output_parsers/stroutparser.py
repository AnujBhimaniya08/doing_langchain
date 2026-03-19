from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
template = PromptTemplate(template="give me detailed report on {topic}", input_variables=['topic'])
prompt = template.invoke({'topic' : 'black hole'})
result = model.invoke(prompt)
template1 = PromptTemplate(template="give me a summary of {text}", input_variables=['text'])
prompt1 = template1.invoke({'text':result.content})
result1 = model.invoke(prompt1)
print(result1.content)
