import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="AI Code Reviewer", page_icon="🧠")
st.title("🧠 AI Code Reviewer & Debug Assistant")

# Load API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("❌ GOOGLE_API_KEY not found in Secrets")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# ✅ STABLE MODEL
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

code_input = st.text_area("Paste your code here", height=300)

if st.button("Analyze Code"):
    if not code_input.strip():
        st.warning("Please enter some code")
    else:
        with st.spinner("Analyzing code..."):
            try:
                response = model.generate_content(
                    f"""
You are a senior software engineer.
Analyze the following code:
1. Explain the logic
2. Find bugs
3. Suggest optimizations
4. Provide improved code

Code:
{code_input}
"""
                )
                st.success("✅ Analysis Complete")
                st.write(response.text)

            except Exception as e:
                st.error(f"❌ Error occurred: {e}")
