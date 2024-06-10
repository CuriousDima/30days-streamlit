import io

import streamlit as st

from PyPDF2 import PdfReader
from groq import Groq

_GROQ_API_KEY = st.secrets["GROQ_API_KEY"]


def extract_text(bytesio_data):
    # Open the PDF file
    reader = PdfReader(bytesio_data)

    # Get the number of pages
    number_of_pages = len(reader.pages)
    st.write(f"Number of pages: {number_of_pages}")

    full_text = ""
    # Extract text from each page
    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text = page.extract_text()
        full_text += text
        # st.write(f"Text on page {page_number + 1}:\n{text}")
    return full_text


def summarize(text):
    client = Groq(api_key=_GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Summarize the given text in a single paragraph: '''%s'''"
                % text,
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content


st.title("Upload Files to a server")
uploaded_file = st.file_uploader(
    "Upload your papers here", type="pdf", accept_multiple_files=False
)
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    bytesio_data = io.BytesIO(bytes_data)
    pdf_text = extract_text(bytesio_data)

    # Generate Summary with Llama3-70B
    st.header("Summary:")
    summary = summarize(pdf_text)
    st.write(summary)
