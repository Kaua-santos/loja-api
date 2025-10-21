from fastapi import FastAPI
import funçoes as f

app = FastAPI(title="gerenciador de loja")

@app.get("/")
def home():
    return {"mensagem": "Bom dia - Bem vindo ao gerenciador de lojas do KAUÃ🤣"}

@app.get("/loja")
def catalogo():
    produtos = f.listar_produtos() 
    lista = []
    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome_produto": produto[1],
            "categoria": produto[2],
            "preco": produto[3],
            "quantidade": produto[4]
        })
    return {"loja": lista}


@app.post("/loja/{id_produto}")
def adicionar_produtos(nome_produto: str,categoria: str,preco: float,quantidade: int):
    f.ad_produto(nome_produto,categoria,preco,quantidade)
    return {"mensagem": "Produto adicionado com sucesso!✔"}


@app.put("/loja/{id_produto}")
def atualizar_produto(id_produto: int, novo_preco: float, nova_quantidade: int):
    f.atualizar_preco_quantidade(novo_preco,nova_quantidade,id_produto)
    return {
        "mensagem": f"Produto {id_produto} atualizado com sucesso!",
        "novo_preco": novo_preco,
        "nova_quantidade": nova_quantidade
}

@app.delete("/loja/{id_produto}")
def deletar_produto(id_produto: int):
    produto = f.listar_produtos()
    if produto:
        f.excluir_produto(id_produto)
        return {"mensagem": "Produto deletado ✔"}
    else: 
        return {"erro": "Erro ao deletar produto"}