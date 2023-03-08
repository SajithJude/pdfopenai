import pdfminer
from pdfminer.high_level import extract_pages
import streamlit as st


from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
output_string = StringIO()
# with open('samples/simple1.pdf', 'rb') as fin:
#     extract_text_to_fp(fin, output_string, laparams=LAParams(),
#                         output_type='html', codec=None)

st.write(pdfminer.__version__)  

uploaded_file = st.file_uploader("Choose a file", "pdf")
if uploaded_file is not None:
    txt= extract_text_to_fp(fin, output_string, laparams=LAParams(),
                        output_type='html', codec=None)
    st.markdown(txt,  unsafe_allow_html=True)

    # for page_layout in extract_pages(uploaded_file):
    #     # st.code(page_layout, language='xmlDoc')
    #     for element in page_layout:
    #         st.code(element, language='xmlDoc')