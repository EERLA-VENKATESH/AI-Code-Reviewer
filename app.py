import streamlit as st
import google.generativeai as ai

# Streamlit app title
st.title("VENKATESH AI DS TUTOR 😎")

# Input field for user query
user_prompt = st.text_input("Enter the Query:", placeholder="Type your query here...")

# Button to trigger response generation
btn_click = st.button("Generate Answer")

# Load API key from file
try:
    with open("api.txt", "r") as f:
        key = f.read().strip()
except FileNotFoundError:
    st.error("Google API key file not found. Please ensure 'Google api key.txt' exists.")
    st.stop()

# Configure Google Generative AI with the API key
ai.configure(api_key=key)

# System prompt for the AI model
sys_prompt = """
You are a helpful AI tutor for Data Science.
Students will ask you doubts related to various topics in Data Science.
You are expected to reply in as much detail as possible.
Make sure to take examples while explaining the concepts.
If a student asks a question outside the Data Science scope,
politely decline and suggest they stick to Data Science questions.
"""

# Function to generate the response
def generate_response(prompt):
    try:
        response = ai.generate_text(
            model="models/text-bison-001",  # Use the correct model ID for text generation
            prompt=f"{sys_prompt}\n\nStudent's question: {prompt}",
            temperature=0.7,
            top_p=0.8,
            candidate_count=1
        )
        return response.candidates[0]['output']
    except Exception as e:
        return f"An error occurred while generating the response: {e}"

# Handle button click
if btn_click:
    if user_prompt.strip():  # Ensure query is not empty
        response = generate_response(user_prompt)
        st.write(response)
    else:
        st.warning("Please enter a query to generate an answer.")
