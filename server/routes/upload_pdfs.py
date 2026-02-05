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
