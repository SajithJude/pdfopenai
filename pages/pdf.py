import io
import streamlit as st
from pdfminer.high_level import extract_pages

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTTextBoxHorizontal, LTTextLineHorizontal
from pdfminer.converter import TextConverter, PDFPageAggregator




# Define the Streamlit app

    # Set the title of the app
st.title("PDF Layout Visualizer")
# Allow the user to upload a PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
if pdf_file is not None:
    # Convert the uploaded PDF file into a BytesIO object
    pdf_io = io.BytesIO(pdf_file.read())
    layouts = []
    # Extract the layout information of the PDF file
    for page_layout in extract_pages(pdf_file):
        layouts.append(page_layout)
    # Visualize the layout information of each page
    for i, layout in enumerate(layouts):
        st.header(f"Page {i+1}")
        for element in layout:

            if isinstance(element, (LTTextBoxHorizontal, LTTextLineHorizontal)):

                node_level = len(element.get_text().split())
                                   # Create an expander for the element based on its node level
                with st.beta_expander(f"Node level: {node_level}", expanded=node_level <= 1):

                    st.write(f"{element.get_text().strip()} ({element.x0}, {element.y0}, {element.x1}, {element.y1})")