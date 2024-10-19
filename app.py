import validators, streamlit as st
from langchain.prompts import PromptTemplate

from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain

from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

## streamlit app now

st.set_page_config(page_title="LangChain: Summarize Text From YT or Websites", page_icon="🐦")

st.title(" LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")


## GEt the Groq api key and url to be summarized

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")
    
url = st.text_input("URL", label_visibility="collapsed")

if st.button("Summarize the Content from YT or Website"):
    
    ## validate all the inputs
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide the information")
    elif not validators.url(url):
        st.error("Please enter the valid url, It can be a YT video url or website url")

