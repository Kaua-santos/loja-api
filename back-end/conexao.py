import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

def conectar():
    try:
        conexao = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None, None