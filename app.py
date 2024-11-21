import streamlit as st
import google.generativeai as ai

# Streamlit app title
st.title("VENKATESH AI DS TUTOR 😎")

# Input field for user prompt
user_prompt = st.text_input("Enter the Query:", placeholder="Type your query here...")

# Button to trigger response generation
btn_click = st.button("Generate Answer")

# Load API key
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
In case a student asks any question outside the Data Science scope,
politely decline and tell them to ask questions from the Data Science domain only.
"""

# Check if the button is clicked
if btn_click:
    if user_prompt.strip():  # Check if the user entered a query
        try:
            # Generate response
            response = ai.generate_text(
                model="models/text-bison-001",  # Updated model name
                prompt=user_prompt,
                temperature=0.7,
                top_p=0.9,
                candidate_count=1,
                system_prompt=sys_prompt
            )
            # Display the response
            st.write(response.candidates[0]['output'])
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query to generate an answer.")
