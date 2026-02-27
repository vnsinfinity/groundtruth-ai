from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class RequestData(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "GroundTruth AI Backend Running"}

@app.post("/generate-tasks")
def generate_tasks(data: RequestData):
    prompt = f"""
Break this request into simple real-world verification tasks:

{data.query}

Return:
- 5 clear actionable tasks
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return {"tasks": result["response"]}