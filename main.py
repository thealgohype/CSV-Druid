import streamlit as st
import os
#from streamlit_mic_recorder import mic_recorder, speech_to_text
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from pandasai import SmartDataframe
import pandas as pd

st.sidebar.title("Chat Config")
model = st.sidebar.selectbox("Select the model", [
    "gpt-3.5-turbo", "gpt-4", "claude-sonnet", "claude-opus", "google-gemini"
],
                             placeholder="Select Model")

if model == "gpt-3.5-turbo":
  llm = ChatOpenAI(model="gpt-3.5-turbo",
                   temperature=0.7,
                   api_key=os.environ['oai'])

elif model == "gpt-4":
  llm = ChatOpenAI(model="gpt-4o",
                   temperature=0.7,
                   api_key=os.environ['oai'])

elif model == "claude-sonnet":
  llm = ChatAnthropic(model="claude-3-sonnet-20240229",
                      api_key=os.environ['claude'])

elif model == "claude-opus":
  llm = ChatAnthropic(model="claude-3-opus-20240229",
                      api_key=os.environ['claude'])

elif model == "google-gemini":
  llm = ChatGoogleGenerativeAI(model="gemini-pro",
                               google_api_key=os.environ['gemini'])

file = st.file_uploader(label="Upload your data", type="csv")
st.sidebar.divider()
with st.sidebar.expander(label="Created By:", expanded=True):
  st.sidebar.image(
      "https://lh3.googleusercontent.com/v1fRBZY3mv3MzVmlWWEOU2VSCKpqgppBriaOrjX4FyEqLf2hKNOhcu1kWhjQAXmzD9HlmlQEWs-qIkRa7nbaZzMwO28=w128-h128-e365-rj-sc0x00ffffff"
  )

st.markdown(f" # Data Analysis Assistant\n ### Using: {model}")
prompt = ChatPromptTemplate.from_template("You are a helpful assitant whose main aim is to assist the user in answering their questions to the BEST of your ABILITY AND KNOWLEDGE.If you don't know, just say you don't know. think stpe by step before answering any question. {question}")
memory = ConversationBufferMemory(memory_key="chat_history")

if file is not None:
  df = pd.read_csv(file)
  df1 = SmartDataframe(df=df,config={"llm":llm})
  text = st.text_input("Enter your question") 
  if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

  if text:
    st.write(df1.chat(text))
    st.divider() 
    st.markdown(f" ### Prompt: \n ### ```{text}```")
  else :
    st.write("Press Enter to Proceed")

  state = st.session_state

  if 'text_received' not in state:
      state.text_received = []

  st.divider() 
  if text:
      state.text_received.append(text)




