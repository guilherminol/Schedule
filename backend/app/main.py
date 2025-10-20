from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from typing import List, Dict, Any

app = FastAPI(title="SaúdeConecta API")

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo Pydantic para a query do usuário
class Query(BaseModel):
    text: str

# Carrega a base de conhecimento
try:
    with open("app/knowledge_base.json", "r", encoding="utf-8") as file:
        knowledge_base: List[Dict[str, Any]] = json.load(file)
except Exception as e:
    print(f"Erro ao carregar knowledge_base.json: {e}")
    knowledge_base = []

def find_answer(query: str) -> str:
    """
    Procura uma resposta na base de conhecimento baseado nas palavras-chave
    """
    query = query.lower().strip()
    
    # Procura por correspondência nas keywords
    for item in knowledge_base:
        if any(keyword in query for keyword in item["keywords"]):
            return item["answer"]
    
    # Resposta padrão se nenhuma correspondência for encontrada
    return "Desculpe, não tenho informações específicas sobre isso. Por favor, consulte um profissional de saúde para orientações precisas."

@app.post("/api/chat")
async def chat(query: Query):
    """
    Endpoint para processar as mensagens do usuário e retornar respostas
    """
    if not query.text:
        raise HTTPException(status_code=400, detail="A mensagem não pode estar vazia")

    response = find_answer(query.text)
    return {"response": response}

@app.get("/")
async def root():
    """
    Rota raiz para verificar se a API está funcionando
    """
    return {"message": "SaúdeConecta API está funcionando!"}