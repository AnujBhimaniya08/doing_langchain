from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
class person(BaseModel):
    name : str = Field(description="write down the name of the person")
    age : int = Field(gt=40,description="write down the age of the person")
    city : str = Field(description="Write down the city to which the person belongs")

parser = PydanticOutputParser(pydantic_object=person)
# template = ChatPromptTemplate(template="Give me name, age, city of a fictional character from {country} \n {format_instruction}, CRITCAL : You can be random in this generation", input_variables=['country'], partial_variables={'format_instruction' : parser.get_format_instructions() })
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a creative writer. When asked for characters, avoid clichés. "
               "Choose diverse, lesser-known cities and ensure all numerical constraints are strictly followed."),
    ("human", "Generate a fictional character from {country}.\n\n{format_instructions}\n"
              "Constraint: The character's age MUST be over 40. "
              "Variety: Pick a random city that isn't just the capital.")
])


prompt_with_format = prompt.partial(format_instructions=parser.get_format_instructions())
chain = prompt_with_format | model | parser
result  = chain.invoke({'country' : 'India'})
print(result)