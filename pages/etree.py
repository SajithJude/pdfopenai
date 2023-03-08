import streamlit as st
import io
import PyPDF2
from xml.etree.ElementTree import XML, fromstring, tostring
# create file upload widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# check if file was uploaded
if uploaded_file is not None:
    # read PDF file contents
    file_contents = uploaded_file.read()

    # create PyPDF2 reader object
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_contents))

    # extract text from PDF file
    text = ""
    
    for i in range(len(pdf_reader.pages)):
        
        page = pdf_reader.pages[i]
        text += page.extract_text()

    # create XML tree from text
    root = fromstring(text)

    # display XML tree
    st.write(tostring(root))
