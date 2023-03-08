import io
import streamlit as st
from pdfminer.high_level import extract_pages

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTTextBoxHorizontal, LTTextLineHorizontal
from pdfminer.converter import TextConverter, PDFPageAggregator

import io
from pdfminer.converter import XMLConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import xml.etree.ElementTree as ET
import streamlit as st

def convert_pdf_to_xml(file):
    # Create a resource manager object to store shared resources
    resource_manager = PDFResourceManager()

    # Create a string object to receive the XML data
    out_string = io.StringIO()

    # Create an XML converter object and link it to the output string
    converter = XMLConverter(resource_manager, out_string, codec='utf-8', laparams=None)

    # Create a PDF interpreter object
    interpreter = PDFPageInterpreter(resource_manager, converter)

    # Loop through each page in the PDF file and convert it to XML
    for page in PDFPage.get_pages(file):
        interpreter.process_page(page)

    # Get the XML data from the output string
    xml_data = out_string.getvalue()

    # Close the output string and XML converter objects
    out_string.close()
    converter.close()

    # Return the XML data
    return xml_data


# Define the Streamlit app

    # Set the title of the app
st.title("PDF Layout Visualizer")
# Allow the user to upload a PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
if pdf_file is not None:
    xml_data = convert_pdf_to_xml(pdf_file)
    st.text_area("XML Data", value=xml_data, height=600)
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