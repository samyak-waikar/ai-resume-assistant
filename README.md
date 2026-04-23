# AI Resume Assistant (RAG-based)

An AI-powered web application that allows users to upload a resume and ask questions about it using a Retrieval-Augmented Generation (RAG) pipeline.

## 🚀 Features
- Upload PDF resume
- Extract and process text
- Semantic search using FAISS
- Ask questions like:
  - What are my skills?
  - What experience do I have?
  - What projects have I built?
- Clean React-based UI

## 🧠 Tech Stack
- **Frontend:** React (Vite)
- **Backend:** FastAPI
- **AI/ML:** Transformers, FAISS, Sentence Transformers
- **Other:** Python, JavaScript

## ⚙️ How It Works
1. Upload resume (PDF)
2. Extract text using PyPDF
3. Split into chunks
4. Convert into embeddings
5. Store in FAISS vector database
6. Retrieve relevant chunks based on query
7. Answer using QA model

## 🛠️ Setup Instructions

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

Frontend
cd frontend
npm install
npm run dev