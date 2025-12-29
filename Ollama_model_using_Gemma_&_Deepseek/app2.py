import streamlit as st
from ollama import Client

# ✅ Create client instance (VERY IMPORTANT)
client = Client(host="http://localhost:11434")

st.set_page_config(
    page_title="Custom LLM model by Vaishnavi Chandore - Ollama",
    layout="centered"
)

st.title("Ollama App")  # using deepseek model

prompt = st.text_area("Enter your prompt:", height=200)

if st.button("Generate Response"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model="deepseek-r1:",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.success("Response Generated!")
            st.write(response["message"]["content"])