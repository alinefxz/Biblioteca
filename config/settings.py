# Ferramentas do Python que ajudam a descobrir onde as pastas e arquivos do projeto estão no seu computador.
import os
from pathlib import Path

# BASE_DIR: Descobre qual é a pasta principal (a raiz) do seu projeto. O Django usa isso como ponto de partida para achar tudo.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: É como a "senha mestre" do seu projeto, usada para proteger dados sensíveis e sessões de usuários. 
# Importante: Nunca mostre isso publicamente quando o site for para a internet!
SECRET_KEY = 'django-insecure-8l8o(-2su$6t%k424293i#x672q0$*^itfyi9r32$8j-igo7zf'

# DEBUG: Quando True, se o código der erro, o Django mostra uma tela amarela cheia de detalhes para te ajudar a consertar. 
# Importante: Mude para False antes de colocar o site no ar (produção), senão os visitantes verão seus erros de código.
DEBUG = True

# ALLOWED_HOSTS: Quais endereços de site (ex: www.seusite.com.br) têm permissão para acessar este projeto. 
# Vazio [] significa que ele aceita apenas o acesso local de desenvolvimento (localhost).
ALLOWED_HOSTS = []

# INSTALLED_APPS: São os "aplicativos" ou "módulos" ativados no projeto.
# O Django já traz vários pré-instalados (como o painel 'admin' e sistema de senhas 'auth'). 
# No final da lista está o seu aplicativo customizado chamado 'app'.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

# MIDDLEWARE: São como "seguranças na porta" do seu site. 
# Eles processam quem entra e sai, lidando com segurança contra ataques, mantendo o usuário logado (sessions), etc.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF: Diz ao Django onde está o arquivo que controla os links/rotas principais do site. 
# Neste caso, está na pasta 'config' no arquivo 'urls.py'.
ROOT_URLCONF = 'config.urls'

# TEMPLATES: Configura como o Django vai lidar com o "visual" do site (seus arquivos HTML).
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: Ensina o Django a procurar seus arquivos HTML especificamente dentro da pasta 'app/templates'.
        'DIRS': [
            os.path.join(BASE_DIR, 'app/templates'),
        ],
        'APP_DIRS': True, # Permite que o Django procure templates automaticamente dentro das pastas dos apps.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION: É a porta de entrada padrão para quando você for hospedar o site em servidores reais.
WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES: Configura a conexão com o banco de dados.
# Aqui você está dizendo: "Conecte-se ao PostgreSQL, no banco chamado 'Biblioteca', usando o usuário 'postgres' e a senha '123456' na minha própria máquina (localhost)".
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Biblioteca',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# AUTH_PASSWORD_VALIDATORS: Regras de segurança para a criação de senhas de usuários.
# Eles impedem que o usuário crie senhas curtas demais, senhas muito comuns (ex: "123456") ou iguais ao nome de usuário.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# LANGUAGE_CODE: Idioma padrão do site. 'pt-br' garante que o painel de admin e mensagens de erro fiquem em português.
LANGUAGE_CODE = 'pt-br'

# TIME_ZONE: Fuso horário padrão do site. Garante que os registros de datas e horas no banco usem o horário de Brasília.
TIME_ZONE = 'America/Sao_Paulo'

# USE_I18N: Ativa o sistema de internacionalização (tradução) do Django.
USE_I18N = True

# USE_TZ: Diz para o Django sempre considerar o fuso horário (TIME_ZONE) ao salvar datas.
USE_TZ = True

# STATIC: Configurações para arquivos "estáticos" (arquivos de design CSS, scripts JavaScript e imagens).
# STATIC_URL: É como o link para esses arquivos vai aparecer no navegador do usuário (ex: meusite.com/static/estilo.css)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(STATIC_URL, "static")
# STATICFILES_DIRS: Diz para o Django procurar seus arquivos CSS, JS e imagens customizadas dentro da pasta 'app/static/'.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "app/static/"),
]

# DEFAULT_AUTO_FIELD: Define como o Django vai criar os números de "IDs" (chaves primárias) das suas tabelas de banco de dados automaticamente.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'