from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from typing import List, Dict, Any
from datetime import datetime
import os
from dotenv import load_dotenv
from openai import OpenAI


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = FastAPI(title="SaúdeConecta API")

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração do OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Aviso: OPENAI_API_KEY não configurada. As respostas da IA não estarão disponíveis.")

# Modelo Pydantic para a query do usuário
class Query(BaseModel):
    text: str

# Palavras-chave de alto risco (RF04)
ALERT_KEYWORDS = {
    "dor no peito", "dificuldade de respirar", "falta de ar", 
    "desmaio", "perda de consciência", "pressão no peito",
    "sangramento intenso", "fala arrastada", "rosto caído",
    "convulsão", "parada", "avc", "infarto"
}

# Mensagem padrão de alerta (RF04 e RF06)
ALERT_RESPONSE = {
    "answer": " ATENÇÃO: EMERGÊNCIA MÉDICA \n\n"
             "Os sintomas que você mencionou podem indicar uma condição grave que requer atenção médica imediata.\n\n"
             " RECOMENDAÇÃO URGENTE:\n"
             "1. Ligue para o SAMU: 192\n"
             "2. Ou procure a emergência mais próxima\n\n"
             "O SaúdeConecta não substitui atendimento médico profissional.",
    "is_alert": True
}

# Carrega a base de conhecimento
try:
    # Tenta diferentes caminhos possíveis para o arquivo
    possible_paths = [
        "app/knowledge_base.json",
        "knowledge_base.json",
        "../app/knowledge_base.json"
    ]
    
    for path in possible_paths:
        try:
            with open(path, "r", encoding="utf-8") as file:
                knowledge_base: List[Dict[str, Any]] = json.load(file)
                print(f"Base de conhecimento carregada com sucesso de: {path}")
                break
        except FileNotFoundError:
            continue
    else:  # Se nenhum arquivo foi encontrado
        print("Erro: Arquivo knowledge_base.json não encontrado em nenhum caminho conhecido")
        knowledge_base = []
except Exception as e:
    print(f"Erro ao carregar knowledge_base.json: {e}")
    knowledge_base = []

def check_for_alerts(query: str) -> bool:
    """
    Verifica se o texto contém palavras-chave de alerta
    """
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in ALERT_KEYWORDS)

def get_ai_response(query: str) -> str:
    """
    Obtém uma resposta da IA usando o OpenAI GPT
    """
    try:
        system_prompt = """Você é um assistente de saúde virtual especializado em fornecer informações básicas sobre saúde.
        Mantenha suas respostas concisas, claras e sempre inclua um lembrete de que não substitui um profissional de saúde.
        Foque em informações gerais e preventivas."""

        client = OpenAI()  
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        print(f"Resposta da IA: {ai_response}")
        return f"{ai_response}\n\nLembre-se: Esta é uma resposta gerada por IA e não substitui uma consulta médica profissional."
    except Exception as e:
        print(f"Erro ao obter resposta da IA: {e}")
        return None

def find_answer(query: str) -> Dict[str, Any]:
    """
    Procura uma resposta na base de conhecimento ou usa IA como fallback
    """
    query = query.lower().strip()
    
    # Verifica alertas primeiro
    if check_for_alerts(query):
        return ALERT_RESPONSE
    
    # Procura por correspondência nas keywords
    for item in knowledge_base:
        if any(keyword in query for keyword in item["keywords"]):
            return {"answer": item["answer"], "is_alert": False}
    
    # Se não encontrar na base de conhecimento, usa IA
    ai_response = get_ai_response(query)
    if ai_response:
        return {"answer": ai_response, "is_alert": False}
    
    # Resposta padrão se tudo falhar
    return {
        "answer": "Desculpe, não tenho informações específicas sobre isso. Por favor, consulte um profissional de saúde para orientações precisas.",
        "is_alert": False
    }

@app.post("/api/chat")
async def chat(query: Query):
    """
    Endpoint para processar as mensagens do usuário e retornar respostas
    """
    if not query.text:
        raise HTTPException(status_code=400, detail="A mensagem não pode estar vazia")

    response = find_answer(query.text)
    
    # Log da interação (pode ser útil para análise futura)
    print(f"[{datetime.now()}] Query: {query.text} | Alert: {response.get('is_alert', False)}")
    
    return response

@app.get("/")
async def root():
    """
    Rota raiz para verificar se a API está funcionando
    """
    return {"message": "SaúdeConecta API está funcionando!"}