import validators, streamlit as st
from langchain.prompts import PromptTemplate

from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain

from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader






## streamlit app now

st.set_page_config(page_title="LangChain: Summarize Text From YT or Websites", page_icon="🐦")

st.title("🐦 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")


## GEt the Groq api key and url to be summarized

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")
    ## llm 
    llm = ChatGroq(api_key=groq_api_key, model="Gemma-7b-It", streaming=True)
    
    ## set the prompts now
    prompt = """
    Provide a summary of the following content in 300 words with a nice title and point wise in numbers:
    Content:{text}
    """
    prompt_template = PromptTemplate(input_variables=['text'], template=prompt)
    
url = st.text_input("URL", label_visibility="collapsed")

if st.button("Summarize the Content from YT or Website"):
    
    ## validate all the inputs
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide the information")
    elif not validators.url(url):
        st.error("Please enter the valid url, It can be a YT video url or website url")
        
    else:
        try:
            with st.spinner("waiting..."):
                ## loading the website data (url data)
                if "youtube.com" in url:
                    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
                    
                    
                else:
                    loader = UnstructuredURLLoader(urls=[url], ssl_verify=False, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"})
                data = loader.load()
                
                ## chain for summarisation now
                
                chain = load_summarize_chain(llm, chain_type='stuff', prompt=prompt_template)
                summary_output = chain.run(data)
                st.success(summary_output)
        except Exception as e:
            st.exception(f"Exception:{e}")
