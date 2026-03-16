from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()

st.header("Research tool")
model = ChatOpenAI(model='gpt-4')
paper_input = st.selectbox("select the paper",["Attention is all you need","BERT:Pre-training of Deep Bidirectional Transformers","GPT-3:Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')
#fill the inputs
# prompt = template.invoke({
#     'paper_input' : paper_input,
#     'style_input' : style_input,
#     'length_input' : length_input
# })
#intro to chains

if st.button("Summarise"):
    chain = template | model
    result = chain.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input
    }) # only single invoking using chain
    # result = model.invoke(prompt)
    st.write(result.content)
