from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()

parser = JsonOutputParser()
template = PromptTemplate(template="Give me name, age and city \n {format_instruction} ", input_variables=[], partial_variables={'format_instruction' : parser.get_format_instructions()})
# prompt = template.format()
# result = model.invoke(prompt)
chain = template | model | parser # here parser.parse(result) is automatically called
result = chain.invoke({})
# print(parser.parse(result.content))
print(result)