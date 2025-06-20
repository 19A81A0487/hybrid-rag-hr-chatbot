from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
from vector import RAGRetriever
from temp import template_response

# Initialize FastAPI app
app = FastAPI(title="Hybrid RAG HR Bot API")

# Load data once on startup
retriever = RAGRetriever("employee_dataset.csv")

# Model for POST /chat
class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

# ✅ Root route - so "/" won't show 404
@app.get("/")
def root():
    return {"message": "✅ HR Bot Backend is running. Visit /docs for API documentation."}

# ✅ POST /chat - send HR queries
@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    try:
        results = retriever.search(request.query)
        response_text = template_response(request.query, results)
        return {"response": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ GET /employees/search - filter by skill
@app.get("/employees/search")
def search_employees(skill: str = Query(..., description="Skill to search for")):
    try:
        matches = retriever.df[
            retriever.df['skills'].apply(lambda s: skill.lower() in str(s).lower())
        ]
        return matches.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
