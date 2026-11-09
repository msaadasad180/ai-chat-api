import os

from fastapi import FastAPI

VERSION = os.getenv("APP_VERSION", "0.1.0")

app = FastAPI(
    title="AI Chat API",
    description="Backend API for an AI-powered chatbot.",
    version=VERSION,
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": VERSION,
    }   