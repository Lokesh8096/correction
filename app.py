import streamlit as st
import google.generativeai as genai
import os

# 🔐 Set your Gemini API key securely
# Note: In a real application, you should load this from environment variables or Streamlit secrets
# For this example, it's hardcoded as provided.
GEMINI_API_KEY = st.secrets["GEMINI"]["API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
# 🎯 Set up Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# 🖥️ Streamlit UI
st.set_page_config(page_title="AI-Powered Autocorrect", layout="centered")
st.title(" AI-Powered Autocorrect")
st.write("Type a sentence and click the button to get spelling corrections using Google's Gemini AI:")

# 📥 Input box - Changed to st.text_area
user_input = st.text_area("Enter text with typos:", height=150, key="user_text_input") # Added a key for the text area

# 🚀 Add a button to trigger autocorrection
if st.button("Correct Text", key="correct_button"):
    if user_input:
        with st.spinner("Thinking..."):
            prompt = f"Correct the spelling mistakes in the following text:\n\n'{user_input}'"
            try:
                response = model.generate_content(prompt)
                corrected_text = response.text.strip()
                if corrected_text.lower() != user_input.lower():
                    st.success(f"✅ Suggested Correction:\n\n{corrected_text}")
                else:
                    st.info("🟢 No corrections needed!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please enter some text to correct.")

