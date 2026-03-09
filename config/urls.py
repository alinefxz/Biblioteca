# Importa o módulo do painel de administração (o painel de controle) pronto do Django.
from django.contrib import admin

# Importa as ferramentas 'include' e 'path', que servem para construir e organizar os links (URLs) do seu site.
from django.urls import include, path

# Importa TUDO (todas as funções/telas) que existe dentro do arquivo views.py do seu aplicativo 'app'.
from app.views import *

# Essa é a lista oficial de rotas do seu projeto. O Django sempre olha para cá para saber qual página carregar quando alguém digita um link.
urlpatterns = [
    # Cria o link "seusite.com/admin/". Quando alguém acessar isso, o Django abre o painel de administração.
    path('admin/', admin.site.urls),
]