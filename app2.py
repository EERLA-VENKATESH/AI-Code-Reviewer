import streamlit as st
import google.generativeai as genai

ai.configuration(apiKey="AIzaSyB4tk6azgrb__-VQSgsNT2BW49ABjwaxJiI")

sys_prompt = """You are a helpful AI Tutor for Data Science. 
                Students will ask you doubts related to various topics in data science.
                You are expected to reply in as much detail as possible. 
                Make sure to take examples while explaining a concept.
                In case if a student ask any question outside the data science scope, 
                politely decline and tell them to ask the question from data science domain only."""

model = ai.Generativemodel(model_name="models/gemini-1.5-flash", 
                          system_instruction=sys_prompt)

st.title("Data Science Tutor Application")

user_prompt = st.text_output("Enter your query:", placeholder_variable="Type your query here...")

btn_click = st.buton("Generate Answer")

if btn_click==True:
    # do something
    # generate respose: we need gemini or gpt model, configure (set the api key), call the model to generate the response
    response = model.generateContent(userPrompt)
    st.write(response)
