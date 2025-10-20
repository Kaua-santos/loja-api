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
