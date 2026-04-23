from rag_pipeline import extract_text_from_pdf, create_vector_store,ask_question
from fastapi import FastAPI, File, UploadFile
from isort import file
from matplotlib import text
from rag_pipeline import extract_text_from_pdf
import shutil
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
vector_store = None

UPLOAD_FOLDER = "uploads"

# create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Backend is running successfully!"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global vector_store

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # extract text
    text = extract_text_from_pdf(file_path)

    # create vector store
    vector_store = create_vector_store(text)

    return {
        "message": "File uploaded and processed successfully"
    }

@app.post("/ask")
async def ask(query: str):
    global vector_store

    if vector_store is None:
        return {"error": "Upload resume first"}

    answer = ask_question(vector_store, query)

    return {"answer": answer}