import os
from loguru import logger
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from modules.mem_client import mem_client   # ← EXACT client you created

UPLOAD_DIR = "./uploaded_docs"
ACTIVE_PDF_PATH = os.path.join(UPLOAD_DIR, "active.pdf")

os.makedirs(UPLOAD_DIR, exist_ok=True)

# -------------------------------
# Reset previous memory
# -------------------------------
def reset_memory():
    """
    Clears existing vector memory stored in Qdrant via mem0.
    """
    logger.info("Resetting existing memory")
    mem_client.reset()


# -------------------------------
# Ingest ONE PDF (overwrite mode)
# -------------------------------
def ingest_pdf(upload_file):
    """
    - Deletes previous PDF
    - Clears Qdrant memory via mem0
    - Saves new PDF
    - Chunks and stores content using mem0
    """

    logger.info("Starting PDF ingestion")

    # 1️⃣ Delete previous PDF
    if os.path.exists(ACTIVE_PDF_PATH):
        os.remove(ACTIVE_PDF_PATH)
        logger.info("Previous PDF deleted")

    # 2️⃣ Reset vector memory
    reset_memory()

    # 3️⃣ Save uploaded PDF
    with open(ACTIVE_PDF_PATH, "wb") as f:
        f.write(upload_file.file.read())

    # 4️⃣ Load PDF
    loader = PyPDFLoader(ACTIVE_PDF_PATH)
    documents = loader.load()

    if not documents:
        raise ValueError("No text extracted from PDF")

    # 5️⃣ Chunk text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    if not chunks:
        raise ValueError("No chunks created from PDF")

    # 6️⃣ Store chunks in mem0 (Qdrant + Gemini embeddings)
    for idx, chunk in enumerate(chunks):
        mem_client.add(
            content=chunk.page_content,
            metadata={
                "source": "active.pdf",
                "page": chunk.metadata.get("page"),
                "chunk_id": idx
            }
        )

    logger.info(f"PDF ingestion completed: {len(chunks)} chunks stored")

    return {
        "file": upload_file.filename,
        "chunks_indexed": len(chunks)
    }
