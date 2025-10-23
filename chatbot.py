from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os


from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# --- Configuração OpenAI ---
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("API Key não encontrada. Verifique o .env")

# --- Configuração FastAPI ---
app = FastAPI(title="ChatBot com Memória Persistente")



# --- Configuração banco de dados SQLite ---
DATABASE_URL = "sqlite:///./chatbot.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Modelo do banco ---
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    role = Column(String)  # "user" ou "assistant"
    content = Column(Text)

# Cria tabelas automaticamente
Base.metadata.create_all(bind=engine)

# --- Modelo da requisição ---
class ChatRequest(BaseModel):
    user_id: str
    message: str

# --- Endpoint de chat ---

@app.post("/chat")
async def chat(request: ChatRequest):
    return {"response": f"Você disse: {request.message}"}

@app.post(
    "/chat",
    summary="💬 Chat com Memória",  
    description="Envie mensagens para o chatbot e receba respostas com memória persistente.",
    tags=["Chatbot"]  
)
async def chat(request: ChatRequest):
    return {"response": f"Você disse: {request.message}"}
