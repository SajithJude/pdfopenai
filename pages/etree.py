import streamlit as st
import io
import PyPDF2
import xml.etree.ElementTree as ET

# create file upload widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# check if file was uploaded
if uploaded_file is not None:
    # read PDF file contents
    file_contents = uploaded_file.read()

    # create PyPDF2 reader object
    pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(file_contents))

    # extract text from PDF file
    text = ""
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        text += page.extractText()

    # create XML tree from text
    root = ET.fromstring(text)

    # display XML tree
    st.write(ET.tostring(root))
