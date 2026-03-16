# Importa o módulo de administração do Django,
# que permite gerenciar o banco de dados pelo painel /admin
from django.contrib import admin

# Importa a função path, usada para definir as URLs do projeto
from django.urls import path

# Importa TemplateView, uma view genérica usada para renderizar templates
from django.views.generic import TemplateView

# Importa todas as views definidas no arquivo views.py do app
from app.views import *


# Lista que define todas as rotas (URLs) do projeto
urlpatterns = [

    # Rota para acessar o painel administrativo do Django
    # Exemplo de acesso: /admin
    path('admin/', admin.site.urls),

    # Rota da página inicial do site
    # Quando acessar a URL principal "", chama a IndexView
    path('', IndexView.as_view(), name='index'),

    # Rota para a página de livros
    # Exemplo de acesso: /livros
    path('livros/', LivrosView.as_view(), name='livros'),

    # Rota para a página de reserva / empréstimo de livros
    # Exemplo de acesso: /reserva
    path('reserva/', EmprestimoView.as_view(), name='reserva'),

    # Rota para a página de cidades
    # Exemplo de acesso: /cidade
    path('cidade/', CidadesView.as_view(), name='cidade'),

    # Rota para a página de autores
    # Exemplo de acesso: /autor
    path('autor/', AutoresView.as_view(), name='autor'),

    # Rota para a página de editoras
    # Exemplo de acesso: /editor
    path('editor/', EditorasView.as_view(), name='editora'),

    # Rota para a página de leitores
    # Exemplo de acesso: /leitor
    path('leitor/', LeitoresView.as_view(), name='leitor'),

    # Rota para a página de gêneros literários
    # Exemplo de acesso: /genero
    path('genero/', GenerosView.as_view(), name='genero'),
]