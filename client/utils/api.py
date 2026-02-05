import requests
from config import API_URL


def upload_pdf_api(file):
    return requests.post(
        f"{API_URL}/upload_pdfs/",
        files={"file": (file.name, file.getvalue(), "application/pdf")}
    )

def ask_question(question: str):
    response = requests.post(
        f"{API_URL}/ask/",
        data={"question": question}
    )
    return response.json()
