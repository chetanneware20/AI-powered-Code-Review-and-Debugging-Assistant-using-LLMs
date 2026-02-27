import streamlit as st
from openai import OpenAI
import os

# Page config
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Code Reviewer & Debug Assistant")
st.write("Analyze code, detect bugs, and get optimization suggestions")

# Load API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OPENAI_API_KEY not found in Streamlit Secrets")
    st.stop()

client = OpenAI(api_key=api_key)

# User input
language = st.selectbox("Select Programming Language", ["Python", "C", "Java"])

code_input = st.text_area(
    "Paste your code here",
    height=300,
    placeholder="Enter your source code..."
)

# Analyze button
if st.button("🔍 Analyze Code"):
    if not code_input.strip():
        st.warning("⚠️ Please enter some code.")
    else:
        with st.spinner("Analyzing code..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a senior software engineer and code reviewer."
                        },
                        {
                            "role": "user",
                            "content": f"""
Analyze the following {language} code:
1. Explain what the code does
2. Identify bugs or issues
3. Suggest optimizations
4. Provide improved code

Code:
{code_input}
"""
                        }
                    ]
                )

                st.success("✅ Analysis Complete")
                st.markdown("### 🧠 AI Review")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"❌ Error occurred: {e}")
