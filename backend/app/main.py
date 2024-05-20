from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Message(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(message: Message):
    print(f'Message: {message.message}')
    classifier = pipeline("sentiment-analysis")
    result = classifier(message.message)
    print(f'Result: {result}')
    return {"reply": message.message.upper()}