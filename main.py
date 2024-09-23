import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template="""Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."""

model = OllamaLLM(model="llama3.1")

def getLLMResponse(input_text, blog_style, no_words):
   prompt = ChatPromptTemplate.from_template(template)
   chain = prompt | model
   
   response = chain.invoke({"input_text": input_text, "blog_style": blog_style, "no_words": no_words})
   
   return response
  

st.set_page_config(page_title="Blog Generation", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs")

input_text = st.text_input("Enter blog title")

col1, col2 = st.columns([5, 5])

with col1:
  no_words = st.text_input("Enter number of words")
  
with col2:
  blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Scientists", "Common People"), index=0)  
  
  
submit = st.button("Generate")

if submit:
  st.write(getLLMResponse(input_text, blog_style, no_words))