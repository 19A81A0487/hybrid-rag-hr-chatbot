import streamlit as st
import requests

st.set_page_config(page_title="HR Chatbot", layout="centered")

st.title("🤖 HR Assistant Chatbot")
st.markdown("Ask something like:")
st.code("Find Python developers with 3+ years experience")

query = st.text_input("🧑‍💼 Enter your query:")

if st.button("Submit") and query:
    try:
        response = requests.post("http://localhost:8000/chat", json={"query": query})
        if response.status_code == 200:
            st.markdown("### 💬 HR Assistant Response")
            st.success(response.json()["response"])
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"⚠️ Failed to connect to backend: {e}")
