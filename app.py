import streamlit as st
import google.generativeai as ai

# Title for the Streamlit App
st.title("VENKATESH AI DS TUTOR 😎")

# Input field for user query
user_prompt = st.text_input("Enter the Query:", placeholder="Type your query here...")

# Button to trigger response generation
btn_click = st.button("Generate Answer")

# Load API key from file
f = open("api.txt")
key = f.read()
ai.configure(api_key=key)

# System prompt for the AI model
sys_prompt = """
You are a helpful AI tutor for data science.
Students will ask you doubts related to various topics in Data Science.
You are expected to reply in as much detail as possible.
Make sure to take examples while explaining the concepts.
In case a student asks any question outside the data science scope,
politely decline and tell them to ask the question from data science domain only.
"""

# Check if button is clicked
if btn_click:
    if user_prompt.strip():  # Ensure user entered a query
        try:
            # Generate a response using the AI model
            response = ai.generate_text(
                model="models/text-bison-001",  # Correct model name
                prompt=f"{sys_prompt}\n\nStudent's question: {user_prompt}",
                temperature=0.7,
                top_p=0.9,
                candidate_count=1
            )
            # Display the response
            st.write(response.candidates[0]['output'])
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query to generate an answer.")
