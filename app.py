import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="AI Code Reviewer", page_icon="🧠")
st.title("🧠 AI Code Reviewer & Debug Assistant")

# Load API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("❌ GOOGLE_API_KEY not found in environment")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# ✅ CORRECT MODEL ID
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash-latest"
)

code_input = st.text_area("Paste your code here", height=300)

if st.button("Analyze Code"):
    if code_input.strip() == "":
        st.warning("Please enter some code")
    else:
        with st.spinner("Analyzing code..."):
            try:
                response = model.generate_content(
                    f"Explain, debug, and optimize this code:\n\n{code_input}"
                )
                st.success("✅ Analysis Complete")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error occurred: {e}")
