from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat(user_message: UserMessage):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a helpful copilot assistant."},
            {"role": "user", "content": user_message.message}
        ]
    )
    reply = response['choices'][0]['message']['content']
    return {"response": reply}

from fastapi.responses import FileResponse

@app.get("/")
async def serve_frontend():
    return FileResponse("copilot_frontend.html")

git add main.py
git commit -m "Add root route to serve frontend"
git push origin main
