import streamlit as st
import google.generativeai as ai

# Title of the Streamlit app
st.title("VENKATESH AI DS TUTOR 😎")

# Input field for user query
user_prompt = st.text_input("Enter the Query:", placeholder="Type your query here...")

# Button to trigger the response generation
btn_click = st.button("Generate Answer")

# Read the API key from the file and configure Google Generative AI
try:
    with open("api.txt", "r") as f:
        key = f.read().strip()
    ai.configure(api_key=key)
except FileNotFoundError:
    st.error("API key file not found. Please make sure 'Google api key.txt' exists in the same directory.")

# Define the system prompt
sys_prompt = """
You are a helpful AI tutor for data science.
Students will ask you doubts related to various topics in Data Science.
You are expected to reply in as much detail as possible, taking examples while explaining the concepts.
If a student asks any question outside the Data Science scope, politely decline and ask them to restrict their queries to Data Science topics.
"""

# Handle button click
if btn_click:
    if not user_prompt:
        st.warning("Please enter a query before clicking the button.")
    else:
        try:
            # Generate a response
            response = ai.chat(
                model="models/chat-bison-001",  # Updated model name for compatibility
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_prompt},
                ]
            )
            # Display the response
            st.write(response['candidates'][0]['content'])
        except Exception as e:
            st.error(f"An error occurred: {e}")
