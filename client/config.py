import requests

BASE_URL = "https://medicalassistant-uq7i.onrender.com"


def upload_pdf_api(file):
    return requests.post(
        f"{BASE_URL}/upload_pdfs",
        files={"file": (file.name, file.getvalue(), "application/pdf")}
    )

