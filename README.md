# GenAI-Healthcare-Assistant-

# 🧠 GenAI Healthcare Assistant

A Generative AI-powered assistant that enables internal teams to query and summarize content from internal documents such as healthcare SOPs, policy manuals, and IT handbooks. Built with LangChain, OpenAI, FAISS, and Streamlit, this tool empowers users to get accurate, fast, and context-aware answers from lengthy PDFs—without needing to read the whole document.

---

## 🚨 Problem Statement

Healthcare and enterprise professionals often deal with hundreds of pages of internal documentation—ranging from clinical protocols to IT policies. Manually searching through these documents wastes time and leads to missed or misunderstood information.

---

## 💡 Solution

The **GenAI Healthcare Assistant** solves this by allowing users to upload a document and ask natural language questions. It leverages **LangChain**, **OpenAI’s GPT models**, and **FAISS** to find and return relevant, contextualized answers.

---

## 🔧 Features

- 📄 Upload and process internal PDF documents (e.g., SOPs, manuals)
- 🧠 Embed and store document chunks using OpenAI embeddings + FAISS
- 🔍 Ask natural language questions and get AI-generated, accurate answers
- 📌 Highlights the most relevant text used in the answer (optional for future)
- ⚡ Built with Streamlit for easy use by non-technical staff

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM & Embeddings**: OpenAI GPT + LangChain
- **Vector Store**: FAISS
- **Document Loader**: PyMuPDF (for PDF ingestion)
- **Environment**: Python 3.10+

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
