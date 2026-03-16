# Importa as ferramentas do painel de administração padrão do Django.
from django.contrib import admin

# Importa TUDO (todas as tabelas/classes) do arquivo models.py que está na mesma pasta (por isso o ponto antes de models).
from .models import *

# ==========================================
# REGISTRO DAS TABELAS NO PAINEL
# ==========================================
# Os comandos abaixo pegam as tabelas que você criou no models.py e as "cadastram" no painel azul do Django.
# Sem essas linhas, as tabelas existem no banco de dados, mas não aparecem na tela do site para você gerenciar.

admin.site.register(Cidade)   # Faz a tabela de Cidades aparecer no painel
admin.site.register(Autor)    # Faz a tabela de Autores aparecer no painel
admin.site.register(Editora)  # Faz a tabela de Editoras aparecer no painel
admin.site.register(Leitor)   # Faz a tabela de Leitores aparecer no painel
admin.site.register(Livro)    # Faz a tabela de Livros aparecer no painel
admin.site.register(Genero)   # Faz a tabela de Gêneros aparecer no painel
admin.site.register(Emprestimo)