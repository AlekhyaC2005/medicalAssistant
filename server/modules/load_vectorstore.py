import os
from loguru import logger
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from modules.mem_client import mem_client   # your existing client

# -------------------------------
# Single active PDF (no directory)
# -------------------------------
ACTIVE_PDF_PATH = "active.pdf"


def ingest_pdf(upload_file):
    """
    Upload ONE PDF at a time.
    Each new upload overwrites active.pdf
    """

    logger.info("Starting PDF ingestion")

    # 1️⃣ Reset vector memory (single-document policy)
    mem_client.reset()
    logger.info("Previous vector memory cleared")

    # 2️⃣ Save uploaded PDF as active.pdf
    with open(ACTIVE_PDF_PATH, "wb") as f:
        f.write(upload_file.file.read())

    logger.info("active.pdf saved successfully")

    # 3️⃣ Load PDF
    loader = PyPDFLoader(ACTIVE_PDF_PATH)
    documents = loader.load()

    if not documents:
        raise ValueError("No text could be extracted from the PDF")

    # 4️⃣ Chunk PDF
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    if not chunks:
        raise ValueError("No chunks created from the PDF")

    # 5️⃣ Store chunks in vector memory
    for idx, chunk in enumerate(chunks):
        mem_client.add(
            content=chunk.page_content,
            metadata={
                "source": "active.pdf",
                "page": chunk.metadata.get("page"),
                "chunk_id": idx
            }
        )

    logger.info(f"Ingestion complete: {len(chunks)} chunks stored")

    return {
        "file": upload_file.filename,
        "chunks_indexed": len(chunks)
    }
