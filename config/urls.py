from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [

    # painel admin
    path('admin/', admin.site.urls),

    # página inicial
    path('', IndexView.as_view(), name='index'),

    # página de livros
    path('livros/', LivrosView.as_view(), name='livros'),

    # página de reservas
    path('reserva/', EmprestimoView.as_view(), name='reserva'),

    # cidade
    path('cidade/', CidadesView.as_view(), name='cidade'),

    # autor
    path('autor/', AutoresView.as_view(), name='autor'),

    # editora
    path('editor/', EditorasView.as_view(), name='editora'),

    # leitor
    path('leitor/', LeitoresView.as_view(), name='leitor'),

    # genero
    path('genero/', GenerosView.as_view(), name='genero'),

    # deletar livro
    path('delete/<int:id>/', DeleteLivroView.as_view(), name='delete'),

]