from fastapi import FastAPI
from database import engine, Base
from models import Loan

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Powered Debt Relief & Financial Recovery Platform"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Powered Debt Relief & Financial Recovery Platform"
    }