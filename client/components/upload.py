import streamlit as st
from utils.api import upload_pdf_api


def render_uploader():
    st.sidebar.header("Upload Medical document (.PDF)")

    uploaded_file = st.sidebar.file_uploader(
        "Upload a medical PDF",
        type="pdf",
        accept_multiple_files=False   # ✅ SINGLE FILE
    )

    if st.sidebar.button("Upload DB"):
        if uploaded_file is None:
            st.sidebar.warning("Please upload a PDF first")
            return

        response = upload_pdf_api(uploaded_file)

        if response.status_code == 200:
            st.sidebar.success("Document indexed successfully ✅")
        else:
            st.sidebar.error(f"Error: {response.text}")
