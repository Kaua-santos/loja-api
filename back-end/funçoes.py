from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS loja (
                    id SERIAL PRIMARY KEY,
                    nome_do_produto TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    avaliacao_do_produto REAL
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela: {erro}")
        else: 
            print("deu certo")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()