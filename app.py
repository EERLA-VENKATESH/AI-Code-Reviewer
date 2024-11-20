import streamlit as st
import google.generativeai as ai
st.title("VENKATESH AI DS TUTOR:sunglasses:")
user_prompt=st.text_input("Enter the Query:",placeholder="Type your query here...")
btn_click=st.button("Generate Answer")
f = open("Google api key.txt")
key = f.read()
ai.configure(api_key=key)
sys_prompt="""you are a helpful ai tutor for data science .
            Students will ask you doubts related to various topics in Data Science
            you are expected to reply in as much detail as possible.
            make sure to take examples while explaining the concepts.
            in case if a student ask any question outside the data sciene scope,
            politely decline and tell then to ask the question from data science domasin only."""
model = ai.GenerativeModel(model_name="models/gemini-1.5-flash-8b-latest",system_instruction=sys_prompt)
if btn_click==True:
    response = model.generate_content(user_prompt)
    st.write(response.text)
