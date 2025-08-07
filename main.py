from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  
from pydantic import BaseModel
from email_sender import send_email
from ai_generator import generate_email

app = FastAPI()

# Mount frontend build folder
app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="static")

# Catch-all route to serve index.html for React Router
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    return FileResponse("../frontend/dist/index.html")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

class GenerateRequest(BaseModel):
    prompt: str

class SendEmailRequest(BaseModel):
    recipients: list
    subject: str
    content: str

@app.post("/generate")
def generate(req: GenerateRequest):
    content = generate_email(req.prompt)
    return {"content": content}

@app.post("/send")
def send(req: SendEmailRequest):
    send_email(req.recipients, req.subject, req.content)
    return {"status": "sent"}


@app.post("/send")
def send(req: SendEmailRequest):
    send_email(req.recipients, req.subject, req.content)
    return {"status": "sent"}
