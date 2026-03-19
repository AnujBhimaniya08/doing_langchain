from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
template = PromptTemplate(template="give me detailed report on {topic}", input_variables=['topic'])

template1 = PromptTemplate(template="give me a summary of {text}", input_variables=['text'])


parser = StrOutputParser()
chain = template | model | parser | template1 | model | parser

result = chain.invoke({'topic' : 'black Hole'})
print(result)