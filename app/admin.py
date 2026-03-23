# Importa as ferramentas do painel de administração padrão do Django.
from django.contrib import admin

# Importa todos os models
from .models import *

# ==========================================
# INLINE (Livro dentro do Autor)
# ==========================================
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1 #Número de livros adicionais para adicionar no admin


# ==========================================
# PERSONALIZAÇÃO DO AUTOR
# ==========================================
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',) #Campos que serão exibidos na listagem
    search_fields = ('nome',) #Campos que serão pesquisados
    inlines = [LivroInline] #Add a tabela de livros no admin de gêneros


# ==========================================
# REGISTRO DAS TABELAS
# ==========================================
admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Genero)
admin.site.register(Emprestimo)

# ⚠️ IMPORTANTE:
# Autor e Livro são registrados aqui embaixo corretamente

admin.site.register(Livro)
admin.site.register(Autor, AutorAdmin)