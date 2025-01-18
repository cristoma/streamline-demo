from langchain_openai import ChatOpenAI
import streamlit as st

st.title("Ask Anything")

with st.sidebar:
    st.title("Provide your OpenAI API key")
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")

if not OPENAI_API_KEY:
    st.info("Enter yout OpenAI API key to continue")
    st.stop()

model="gpt-4o-mini"

llm = ChatOpenAI(temperature=0, model=model, api_key=OPENAI_API_KEY)
question = st.text_input("Enter the question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)

