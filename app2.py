import streamlit as st
import google.generativeai as ai
import os  # for environment variables

# Get API key from environment variable
api_key = os.environ.get("AIzaSyB2VQdpRcKov0og09h3PndHI_q2IQBaAZQ")
if api_key is None:
    st.error("Please set the GOOGLE_GENERATIVE_AI_API_KEY environment variable.")
    st.stop()

ai.configure(api_key=api_key)

sys_prompt = """You are a helpful AI Tutor for Data Science. 
                Students will ask you doubts related to various topics in data science.
                You are expected to reply in as much detail as possible. 
                Make sure to take examples while explaining a concept.
                In case if a student asks any question outside the data science scope, 
                politely decline and tell them to ask the question from the data science domain only."""

model = ai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                          system_instruction=sys_prompt)

st.title("Data Science Tutor Application")

user_prompt = st.text_input("Enter your query:", placeholder="Type your query here...")

btn_click = st.button("Generate Answer")

if btn_click:
    if not user_prompt:
        st.warning("Please enter a query.")
    else:
        try:
            response = model.generate_text(prompt=user_prompt, model="models/gemini-1.5-flash", temperature=0.7) # Assuming generate_text is the correct method; Check API docs
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
