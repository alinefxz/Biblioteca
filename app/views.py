# Importa atalhos úteis do Django: 
# 'render' para desenhar a página HTML na tela, 
# 'redirect' para mandar o usuário para outro link,
# 'get_object_or_404' para buscar algo no banco de dados e dar erro 404 se não achar.
from django.shortcuts import render, redirect, get_object_or_404

# Importa todas as tabelas (Livro, Autor, etc.) que você criou no arquivo models.py.
from .models import *

# Importa a classe 'View', que é a base para criar páginas no formato de "Classes" no Django.
from django.views import View

# Importa o sistema de mensagens para mostrar avisos na tela (ex: "Livro salvo com sucesso!").
from django.contrib import messages

# ==========================================
# PÁGINA INICIAL (Index)
# ==========================================
# Cria a página principal do site, chamando ela de 'IndexView'. Ela usa a base 'View' do Django.
class IndexView(View):
    
    # O método GET define o que acontece quando o usuário simplesmente acessa o link da página no navegador.
    def get(self, request, *args, **kwargs):
        # Manda o Django procurar o arquivo 'index.html' (na pasta templates) e mostrar para o usuário.
        return render(request, 'index.html')

    # O método POST define o que acontece quando o usuário envia dados escondidos (ex: clica em "Salvar" num formulário).
    def post(self, request):
        # O 'pass' significa "passe reto" ou "não faça nada por enquanto". 
        # É só um espaço reservado para você escrever o código de salvar o formulário no futuro.
        pass