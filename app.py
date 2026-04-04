from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import model

app = FastAPI()

class RequestData(BaseModel):
    prompt: str
    max_tokens: int = 50

@app.on_event("startup")
async def startup():
    model.load_model()

@app.get("/")
def root():
    return {
        "info": "Text Generation API using LiquidAI LFM-350M",
        "status": "Online"
    }

@app.get("/health")
def health():
    if model.llm is not None:
        return {"status": "ready"}
    return {"status": "loading or failed"}

@app.post("/generate")
async def predict(data: RequestData):
    if not data.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    response = model.generate_answer(data.prompt, data.max_tokens)
    
    if "Error" in response:
        raise HTTPException(status_code=500, detail=response)
        
    return {
        "prompt": data.prompt,
        "result": response
    }