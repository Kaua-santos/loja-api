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

def atualizar_preco_quantidade(preco, quantidade, id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE loja SET preco = %s, quantidade = %s WHERE id = %s",
                (preco, quantidade, id_produto)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar preço e quantidade do produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def excluir_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute(
                "DELETE FROM loja WHERE id = %s", (id_produto,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao deletar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def valor_total_estoque():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT SUM(preco * quantidade) FROM loja"
            )
            resultado = cursor.fetchone()
            return resultado[0] if resultado[0] is not None else 0
        except Exception as erro:
            print(f"Erro ao calcular valor total do estoque: {erro}")
            return 0
        finally:
            cursor.close()
            conexao.close()
