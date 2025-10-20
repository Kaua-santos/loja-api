import streamlit as s
import requests as r

API_URL = "http://127.0.0.1:8000"

s.set_page_config(page_title="Loja do Kauã 🤣", page_icon="🙅‍♂️")

s.title("🥱 SANTOS SHOP 🥱")

menu = s.sidebar.radio('Opções', ["Produtos", "Adicionar produto", "Atualizar produto", "Deletar produto"])

if menu == "Produtos":
    s.subheader("Todos os produtos")
    response = r.get(f"{API_URL}/loja")
    if response.status_code == 200:
        produtos = response.json().get("loja", [])
        if produtos:
            for produto in produtos:
                s.write(f"**{produto['nome_produto']}** ({produto['categoria']}) - R$ {produto['preco']} - Quantidade: {produto['quantidade']}")
        else:
            s.info("Nenhum produto encontrado")
    else:
        s.error("Erro ao conectar com a API")

elif menu == "Adicionar produto":
    s.subheader('➕ Adicionar produto')
    nome = s.text_input("Nome do produto")
    categoria = s.text_input("Categoria")
    preco = s.number_input("Preço", min_value=0.0, step=0.01, format="%.2f")
    quantidade = s.number_input("Quantidade", min_value=0, step=1)

    if s.button("Salvar produto"):
        params = {
            "nome_produto": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        }
        response = r.post(f"{API_URL}/loja/{0}", params=params)
        if response.status_code == 200:
            s.success("Produto adicionado com sucesso")
        else:
            s.error("Erro ao adicionar o produto")
