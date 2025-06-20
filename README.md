🧠 app.py - FastAPI Backend Overview

✅ Purpose:
The app.py file builds a REST API backend for the HR chatbot using FastAPI.
It connects the frontend (Streamlit or Swagger UI) with the semantic search engine and employee data.

📁 employee_dataset.csv

The employee_dataset.csv file contains sample employee data including name, skills, years of experience, past projects, and availability.
It is used as the data source for semantic search and matching employees based on HR queries.

📄 temp.py – Response Template Generator

✅ Purpose:
temp.py formats the matched employee records into a clean, readable natural language response — without using an LLM.

📄 vector.py – Semantic Search Engine

✅ Purpose:
vector.py contains the logic to convert employee profiles into embeddings, build a FAISS vector index, and retrieve the most relevant employees for a given HR query.

📄 frontend.py – Streamlit Chat Interface

✅ Purpose:
frontend.py provides a simple web-based chat UI using Streamlit, where HR users can enter queries and get smart employee recommendations.
