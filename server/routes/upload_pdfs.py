# routes/upload_pdfs.py
from fastapi import APIRouter, UploadFile, File
from modules.load_vectorstore import ingest_pdf

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    result = ingest_pdf(file)
    return {
        "message": "PDF uploaded successfully",
        **result
    }

def ask_question(question: str):
    response = requests.post(
        f"{API_URL}/ask",
        data={"question": question}
    )
    return response.json()
