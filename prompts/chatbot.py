from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
# chat_history = {"users" : [], "ai" : []}
chat_history = [SystemMessage(content='You are really helpful AI Assistant')]
while True:
    user_input = input("you : ")
    if(user_input == 'exit'):
        break
    # chat_history["users"].append(user_input)
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    # chat_history["ai"].append(result.content)
    chat_history.append(AIMessage(content=result.content))
    print('AI:', result.content)
print(chat_history)