# Importa a biblioteca 'models' do Django. Ela tem as ferramentas para criar as tabelas do banco de dados.
from django.db import models

# ==========================================
# TABELA: CIDADE
# ==========================================
# Cria a tabela "Cidade". O "(models.Model)" avisa o Django que isso vai virar uma tabela no banco.
class Cidade(models.Model):
    # Cria a coluna 'nome' para textos (CharField) de até 100 caracteres.
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    
    # Cria a coluna 'uf' para a sigla do estado (ex: SP, MG).
    uf = models.CharField(max_length=2, verbose_name="UF")

    # Define como a cidade será exibida no painel
    def __str__(self):
        return f"{self.nome}, {self.uf}"

    # Configurações extras
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


# ==========================================
# TABELA: AUTOR
# ==========================================
class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do autor")
    
    # Relaciona o autor com uma cidade
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do autor")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


# ==========================================
# TABELA: EDITORA
# ==========================================
class Editora(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da editora")
    site = models.CharField(max_length=100, verbose_name="Site da editora")
    
    # Relaciona com cidade
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da editora")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"


# ==========================================
# TABELA: LEITOR
# ==========================================
class Leitor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do leitor")
    email = models.CharField(max_length=100, verbose_name="Email do leitor")
    
    # CPF único (não pode repetir)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do leitor")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"


# ==========================================
# TABELA: GÊNERO
# ==========================================
class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Gênero")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"


# ==========================================
# TABELA PRINCIPAL: LIVRO
# ==========================================
class Livro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do livro")
    
    # Relacionamentos
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor do livro")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora do livro")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero do livro")
    
    # Campo numérico (inteiro)
    preco = models.IntegerField(verbose_name="Preço do livro")
    
    # Data de publicação
    data_plub = models.DateField(verbose_name="Data de publicação do livro")
    
    # Status (True/False)
    status = models.BooleanField(verbose_name="Status do livro")

    def __str__(self):
        return f'{self.nome}, {self.autor}'

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"


# ==========================================
# TABELA: EMPRÉSTIMO / RESERVA
# ==========================================
class Emprestimo(models.Model):

    # Liga o empréstimo ao livro
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")

    # Liga ao leitor
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE, verbose_name="Leitor")

    # Datas
    data_emprestimo = models.DateField(verbose_name="Data do empréstimo")
    data_devolucao = models.DateField(verbose_name="Data de devolução")

    def __str__(self):
        return f'{self.livro} - {self.leitor}'

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"