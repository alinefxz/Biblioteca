# Importa a biblioteca 'models' do Django. Ela tem as ferramentas para criar as tabelas do banco de dados.
from django.db import models

# ==========================================
# TABELA: CIDADE
# ==========================================
# Cria a tabela "Cidade". O "(models.Model)" avisa o Django que isso vai virar uma tabela no banco.
class Cidade(models.Model):
    # Cria a coluna 'nome' para textos (CharField) de até 100 caracteres. 'verbose_name' é o nome bonitinho que aparece na tela.
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    # Cria a coluna 'uf' para a sigla do estado, limitando a 2 caracteres (ex: SP, MG).
    uf = models.CharField(max_length=2, verbose_name="UF")

    # Esta função diz ao Django como mostrar essa Cidade em formato de texto lá no painel.
    def __str__(self):
        # Junta o nome e a UF. Exemplo de resultado: "São Paulo, SP"
        return f"{self.nome}, {self.uf}"

    # A classe Meta guarda configurações extras de como a tabela será chamada no painel administrativo.
    class Meta:
        verbose_name = "Cidade" # Nome no singular
        verbose_name_plural = "Cidades" # Nome no plural

# ==========================================
# TABELA: AUTOR
# ==========================================
class Autor(models.Model):
    # Coluna de texto para o nome do autor (até 100 caracteres).
    nome = models.CharField(max_length=100, verbose_name="Nome do autor")
    
    # ForeignKey cria uma "Chave Estrangeira". Isso liga o Autor a uma Cidade existente.
    # on_delete=models.CASCADE significa: se a Cidade for apagada do banco, apague todos os autores dela junto.
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do autor")

    # Quando precisar mostrar o autor, mostra apenas o nome dele.
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

# ==========================================
# TABELA: EDITORA
# ==========================================
class Editora(models.Model):
    # Coluna para o nome da editora.
    nome = models.CharField(max_length=100, verbose_name="Nome da editora")
    # Coluna para o site da editora.
    site = models.CharField(max_length=100, verbose_name="Site da editora")
    # Liga a Editora a uma Cidade, apagando a editora caso a cidade seja deletada (CASCADE).
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da editora")

    # Mostra o nome da editora como representação de texto.
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"

# ==========================================
# TABELA: LEITOR
# ==========================================
class Leitor(models.Model):
    # Nome do leitor.
    nome = models.CharField(max_length=100, verbose_name="Nome do leitor")
    # Email do leitor.
    email = models.CharField(max_length=100, verbose_name="Email do leitor")
    # Coluna do CPF. O 'unique=True' é muito importante: impede que duas pessoas usem o mesmo CPF no banco.
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do leitor")

    # Mostra o nome do leitor no painel.
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"

# ==========================================
# TABELA: GÊNERO
# ==========================================
class Genero(models.Model):
    # Nome do gênero do livro (ex: Terror, Romance).
    nome = models.CharField(max_length=100, verbose_name="Gênero")

    # Representação visual da classe.
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

# ==========================================
# TABELA PRINCIPAL: LIVRO
# ==========================================
class Livro(models.Model):
    # Nome do livro.
    nome = models.CharField(max_length=100, verbose_name="Nome do livro")
    
    # Liga o Livro ao Autor correspondente.
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor do livro")
    # Liga o Livro à Editora.
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora do livro")
    # Liga o Livro ao Gênero literário.
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero do livro")
    
    # IntegerField cria uma coluna para guardar números inteiros (sem vírgula).
    # *Dica: Se você quiser usar moedas com centavos (R$ 29,90), o ideal no Django é trocar para models.DecimalField.
    preco = models.IntegerField(verbose_name="Preço do livro")
    
    # DateField é uma coluna feita especificamente para guardar datas (Dias, Meses e Anos).
    data_plub = models.DateField(verbose_name="Data de publicação do livro")
    
    # BooleanField guarda informações de Verdadeiro/Falso. Pode ser usado para "Disponível" / "Indisponível".
    status = models.BooleanField(verbose_name="Status do livro")

    # Mostra o livro de uma forma muito legal no painel: "Nome do Livro, Autor"
    def __str__(self):
        return f'{self.nome}, {self.autor}'

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"