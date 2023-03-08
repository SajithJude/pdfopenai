import streamlit as st
import openai

import os

openai.api_key =  os.getenv("API_KEY")

nat = st.text_input("Enter the query in natural language ")


response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Generate an SQL query from this natural language query to show top 5 tools :" + str(nat) + "  , for a database consisting of 1200 tools related to AI",
            temperature=0.56,
            max_tokens=2066,
            top_p=1,
            frequency_penalty=0.35,
            presence_penalty=0
            
            )
st.code(response.choices[0].text)