import os
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyMuPDFLoader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load documents
@st.cache_data
def load_docs(file_path):
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return text_splitter.split_documents(documents)

# Embed and build vector store
@st.cache_resource
def build_vectorstore(docs):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)

# Streamlit UI
st.title("GenAI Healthcare Assistant")
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])
query = st.text_input("Ask a question based on the document")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    docs = load_docs("temp.pdf")
    vectordb = build_vectorstore(docs)
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        retriever=vectordb.as_retriever()
    )

    if query:
        response = qa_chain.run(query)
        st.write("Answer:")
        st.success(response)
