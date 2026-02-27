import streamlit as st
import google.generativeai as genai
import os

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Code Reviewer & Debug Assistant")
st.write("Analyze code, detect bugs, and get optimization suggestions using GenAI")

# -------------------- API KEY --------------------
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found. Please add it in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# -------------------- USER INPUT --------------------
language = st.selectbox(
    "Select Programming Language",
    ["Python", "C", "Java"]
)

code_input = st.text_area(
    "Paste your code here",
    height=300,
    placeholder="Enter your source code..."
)

# -------------------- ANALYZE BUTTON --------------------
if st.button("🔍 Analyze Code"):
    if code_input.strip() == "":
        st.warning("⚠️ Please enter some code to analyze.")
    else:
        with st.spinner("Analyzing code..."):
            try:
                prompt = f"""
You are a senior software engineer.

Analyze the following {language} code and provide:
1. Explanation of what the code does
2. Bugs or issues (if any)
3. Optimization suggestions
4. Improved version of the code (if applicable)

Code:
{code_input}
"""
                response = model.generate_content(prompt)
                st.success("✅ Analysis Complete")

                st.markdown("### 🧠 AI Review")
                st.write(response.text)

            except Exception as e:
                st.error(f"❌ Error occurred: {e}")
