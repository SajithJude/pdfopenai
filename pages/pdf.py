import io
import streamlit as st
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTTextBoxHorizontal, LTTextLineHorizontal
from pdfminer.converter import TextConverter, PDFPageAggregator


def extract_layout(pdf_path):
    # Open the PDF file
    # with open(pdf_path, 'rb') as fp:
        # Create a PDF parser object
    parser = PDFParser(pdf_path)
    # Create a PDF document object
    doc = PDFDocument(parser)
    # Create a PDF resource manager object
    rsrcmgr = PDFResourceManager()
    # Set parameters for analysis
    laparams = LAParams()
    # Create a PDF device object
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # Create a PDF interpreter object
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Extract the layout information of each page
    layouts = []
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        layouts.append(layout)
    return layouts


# Define the Streamlit app

    # Set the title of the app
st.title("PDF Layout Visualizer")
# Allow the user to upload a PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
if pdf_file is not None:
    # Convert the uploaded PDF file into a BytesIO object
    pdf_io = io.BytesIO(pdf_file.read())
    # Extract the layout information of the PDF file
    layouts = extract_layout(pdf_io)
    # Visualize the layout information of each page
    for i, layout in enumerate(layouts):
        st.header(f"Page {i+1}")
        for element in layout:
            if isinstance(element, (LTTextBoxHorizontal, LTTextLineHorizontal)):
                st.write(f"{element.get_text().strip()} ({element.x0}, {element.y0}, {element.x1}, {element.y1})")
