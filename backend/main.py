from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# --- CONFIGURATION ---
# PASTE YOUR KEY BELOW
GEMINI_API_KEY = "PASTE_YOUR_API_KEY_HERE"

genai.configure(api_key=GEMINI_API_KEY)

# We use "gemini-1.5-flash" because it is fast and free
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="You are a helpful and polite KFC Customer Service Assistant. helping customers with orders, complaints, and menu questions. Keep answers short."
)

class ChatRequest(BaseModel):
    message: str
    user_id: str = "guest"

@app.get("/")
def read_root():
    return {"message": "KFC AI Backend is online"}

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message
    
    try:
        # Send message to Gemini
        response = model.generate_content(user_message)
        ai_reply = response.text
        
        return {"reply": ai_reply}
        
    except Exception as e:
        return {"reply": "Sorry, I am having trouble connecting to the AI right now.", "error": str(e)}

