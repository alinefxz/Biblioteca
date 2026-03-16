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

class IndexView(View):  # cria uma view chamada IndexView que herda de View
    def get(self, request, *args, **kwargs):  # método que responde às requisições GET (quando alguém acessa a página)
        return render(request, 'index.html')  # renderiza (abre) o template index.html


class LivrosView(View):  # view responsável pela página de livros
    def get(self, request, *args, **kwargs):  # executa quando a página é acessada
        livros = Livro.objects.all()  # busca todos os registros do modelo Livro no banco de dados
        return render(request, 'livros.html', {'livros': livros})  # envia os livros para o template livros.html

    # def post(self, request, *args, **kwargs):  # método comentado que seria usado para requisições POST (ex: envio de formulário)


class EmprestimoView(View):  # view responsável pela página de empréstimos/reservas
    def get(self, request, *args, **kwargs):  # executa quando a página é acessada
        reservas = Emprestimo.objects.all()  # busca todos os registros do modelo Emprestimo
        return render(request, 'reserva.html', {'reservas': reservas})  # envia os dados para o template reserva.html


class CidadesView(View):  # view da página de cidades
    def get(self, request, *args, **kwargs):  # executa quando a página é acessada
        cidades = Cidade.objects.all()  # busca todas as cidades cadastradas no banco
        return render(request, 'cidade.html', {'cidades': cidades})  # envia a lista de cidades para o template


class AutoresView(View):  # view da página de autores
    def get(self, request, *args, **kwargs):  # executa quando a página é acessada
        autores = Autor.objects.all()  # busca todos os autores no banco
        return render(request, 'autor.html', {'autores': autores})  # envia os autores para o template


class EditorasView(View):  # view da página de editoras
    def get(self, request, *args, **kwargs):  # executa quando a página é acessada
        editoras = Editora.objects.all()  # busca todas as editoras cadastradas
        return render(request, 'editora.html', {'editoras': editoras})  # envia os dados para o template


class LeitoresView(View):  # view da página de leitores
    def get(self, request, *args, **kwargs):  # executa quando a página é acessada
        leitores = Leitor.objects.all()  # busca todos os leitores no banco
        return render(request, 'leitor.html', {'leitores': leitores})  # envia os leitores para o template


class GenerosView(View):  # view da página de gêneros de livros
    def get(self, request, *args, **kwargs):  # executa quando a página é acessada
        generos = Genero.objects.all()  # busca todos os gêneros cadastrados
        return render(request, 'genero.html', {'generos': generos})  # envia os gêneros para o template
    
# Classe responsável por deletar (excluir) um livro do banco de dados
class DeleteLivroView(View):

    # Método executado quando a página é acessada via requisição GET
    def get(self, request, id, *args, **kwargs):

        # Busca no banco de dados o livro que possui o id informado na URL
        livro = Livro.objects.get(id=id)

        # Exclui o livro encontrado do banco de dados
        livro.delete()

        # Envia uma mensagem de sucesso para o usuário informando que o livro foi excluído
        messages.success(
            request,
            'Livro excluído com sucesso!'  # mensagem exibida após a exclusão
        )

        # Redireciona o usuário de volta para a página de listagem de livros
        return redirect('livros')
    
class ConsultaView(View):

    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})


class ReservaView(View):

    def get(self, request, *args, **kwargs):
        reservas = Emprestimo.objects.all()
        return render(request, 'reserva.html', {'reservas': reservas})