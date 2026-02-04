# 🩺 AI Medical Assistant Chatbot — RAG-Based Application

🔗 **Live App:** https://medicalassistantwithrag.streamlit.app/

---

## 🧠 Project Overview

The **AI Medical Assistant Chatbot** is a Retrieval-Augmented Generation (RAG)–based application designed to help users **query medical documents safely and accurately**.

Users can upload medical PDFs (reports, notes, textbooks), and the system:
1. Retrieves the most relevant document chunks using semantic search
2. Generates answers **strictly grounded in retrieved content**
3. Avoids hallucinations, diagnoses, and treatment advice

⚠️ **Disclaimer:** This application is intended for **educational and informational purposes only** and should not be used for medical diagnosis or treatment decisions.

---

## 🔄 System Architecture


User Query
↓
Query Embedding
↓
Pinecone Vector Database
↓
Relevant Document Chunks
↓
RAG Pipeline (LCEL + Groq LLaMA 3.1)
↓
Context-Grounded Answer



---

## ✨ Key Features

- 📄 Upload medical PDFs (reports, textbooks, notes)
- ✂️ Automatic text extraction and semantic chunking
- 🔎 Vector search using Pinecone
- 🧠 LLaMA-3.1-8B-Instant via Groq for fast inference
- 🛡️ Medical-safe prompting (no diagnosis or treatment advice)
- ⚡ FastAPI backend for ingestion and Q&A
- 🎨 Streamlit frontend for interactive chat

---

## 🧪 Medical Safety Measures

- Answers generated **only from retrieved document context**
- Explicit refusal when information is not found
- No diagnosis or treatment recommendations
- Low-temperature inference to reduce hallucinations

---

## 🧰 Tech Stack

| Component | Technology |
|---------|-----------|
| LLM | Groq API (LLaMA-3.1-8B-Instant) |
| Embeddings | HuggingFace SentenceTransformers (MiniLM) |
| Vector DB | Pinecone |
| RAG Framework | LangChain (LCEL / RunnableSequence) |
| Backend | FastAPI |
| Frontend | Streamlit |
| Deployment | Render |

---

## 📡 API Endpoints

### 📤 Upload PDFs


Uploads one or more medical PDF documents for ingestion.

### ❓ Ask a Question


Form field: `question`  
Returns a context-grounded answer.

---

## 📁 Project Structure


medicalAssistant/
├── client/
│ ├── components/
│ │ ├── chatUI.py
│ │ ├── upload.py
│ │ └── history_download.py
│ ├── utils/
│ │ └── api.py
│ ├── app.py
│ ├── config.py
│ └── requirements.txt
│
├── server/
│ ├── middlewares/
│ │ └── exception_handlers.py
│ ├── modules/
│ │ ├── llm.py
│ │ ├── load_vectorstore.py
│ │ ├── pdf_handlers.py
│ │ └── query_handlers.py
│ ├── routes/
│ │ ├── upload_pdfs.py
│ │ └── ask_question.py
│ ├── uploaded_docs/
│ │ └── demo_medical_report.pdf
│ ├── logger.py
│ ├── main.py
│ └── requirements.txt
│
├── .gitignore
├── README.md
├── pyproject.toml
└── main.py


---

## ⚡ Quick Setup (Local)

### 1️⃣ Clone the Repository
``` bash
git clone https://github.com/AlekhyaC2005/medicalAssistant.git
cd medicalAssistant
```

### 2️⃣ Backend Setup (FastAPI)
cd server
uv venv
.venv/bin/activate   # Windows: venv\Scripts\activate
uv pip install -r requirements.txt



Create .env:

GROQ_API_KEY=your_groq_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX_NAME=medicalindex


Run the server:

uvicorn main:app --reload --port 8000

### 3️⃣ Frontend Setup (Streamlit)
cd ../client
uv venv
.venv/bin/activate
uv pip install -r requirements.txt
streamlit run app.py

### 🚀 Deployment (Render)

Start Command:

uvicorn main:app --host 0.0.0.0 --port 10000


Ensure environment variables are configured in Render dashboard.

### 🧠 Design Highlights

Uses LCEL (RunnableSequence) instead of deprecated RetrievalQA

Custom retriever abstraction for Pinecone results

Local embeddings to avoid API rate limits

Clear separation of client and server responsibilities

### 🌟 Credits

Built by Alekhya Chatterjee
Inspired by the LangChain, Groq, Pinecone, and FastAPI ecosystems.
