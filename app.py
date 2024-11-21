import streamlit as st
import google.generativeai as ai

# Configure the API key
ai.configuration(api_key="AIzaSyDv3ygxyKSxcEXJCrC7sp6up7Sbvuyhfh0")

# System prompt for the AI model
sys_prompt = """
You are a helpful AI tutor for Java programming.
Students will ask you questions related to various topics in Java.
You are expected to reply in as much detail as possible.
Make sure to take examples while explaining concepts.
If a student asks a question outside the Java programming domain,
politely decline and tell them to ask questions related to Java programming only.
"""

# Model configuration
model = ai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    system_instruction=sys_prompt
)

# Streamlit app
st.title("Java Programming Tutor Application")

# Input field for user prompt
user_prompt = st.text_input("Enter your query:", placeholder="Type your query here...")

# Button to trigger response generation
btn_click = st.button("Generate Answer")

# Check if button is clicked
if btn_click:
    if user_prompt.strip():  # Ensure the user entered a query
        try:
            # Generate response using the AI model
            response = model.generate_content(user_prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query to generate an answer.")
