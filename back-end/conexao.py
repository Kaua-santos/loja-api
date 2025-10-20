import psycopg2 as ps
from dotenv import load_dotenv
import os 

# carregar variaveis 
load_dotenv()

params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

def conectar():
    try:
        conexao = ps.connect(**params)
        cursor = conexao.cursor()
        print("deu certo!")
        return conexao, cursor
    except Exception as erro:
        print(f"erro de conexao{ erro}")
        return None, None