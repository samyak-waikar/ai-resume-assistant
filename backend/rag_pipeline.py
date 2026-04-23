from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
from transformers import pipeline
import re

# Step 1: Extract text
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    # CLEAN TEXT
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")

    return text

# Step 2: Create vector store (RAG)
def create_vector_store(text):
    # split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)

    # create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # store in FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    return vector_store

# Better QA model (much better than GPT2)
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def ask_question(vector_store, query):
    docs = vector_store.similarity_search(query, k=3)
    context = " ".join([doc.page_content for doc in docs])

    # CLEAN TEXT
    context = context.replace("\n", " ")
    context = re.sub(r"\s+", " ", context)

    # SPECIAL CASE: Skills
    if "skill" in query.lower():
        skills_section = ""

        # Try extracting after "Skills"
        if "Skills" in context:
            skills_section = context.split("Skills")[1]

        # Stop at next section
        stop_words = ["Experience", "Projects", "Education", "Certifications"]
        for word in stop_words:
            if word in skills_section:
                skills_section = skills_section.split(word)[0]

        return skills_section.replace(":", ":\n")

    # Default QA
    result = qa_pipeline({
        "question": query,
        "context": context
    })

    return result["answer"]
    
