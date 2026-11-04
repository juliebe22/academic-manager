import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("A variável MONGODB_URI não foi configurada no .env")

# Conexão
client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000
)

# Testar conexão
client.admin.command("ping")

# Criar banco de dados
db = client["academic_manager"]

# Criar coleção de alunos
alunos_collection = db["alunos"]

# Garantir que não existam matrículas duplicadas
alunos_collection.create_index("matricula", unique=True)

print("Conectado ao MongoDB Atlas com sucesso!")