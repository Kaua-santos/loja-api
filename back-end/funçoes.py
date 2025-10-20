from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS loja (
                    id SERIAL PRIMARY KEY,
                    nome_do_produto TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    preco DECIMAL,
                    quantidade INT
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

def ad_produto(nome_do_produto,categoria,preco,quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO loja (nome_do_produto,categoria,preco,quantidade)  VALUES (%s, %s,%s,%s)",
                (nome_do_produto,categoria,preco,quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao adiconar produto {erro}")
        else:
            print("produto adicionado com sucesso!✔")
        finally:
            cursor.close()
            conexao.close()

def listar_produtos():
    conexao, cursor = conectar()
    if conexao: 
        try:
            cursor.execute(
                "SELECT * FROM loja ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar filmes {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()
