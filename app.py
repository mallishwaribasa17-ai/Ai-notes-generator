import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Notes Generator",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Notes Generator")
st.write("Upload your study material and generate easy notes using AI.")

uploaded_file = st.file_uploader(
    "📄 Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    st.success("PDF uploaded successfully!")

    st.subheader("📖 Extracted Text")
    st.text_area(
        "Document Content",
        text,
        height=300
    )