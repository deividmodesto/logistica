from django.contrib import admin
from django.urls import path, include  # Certifique-se de que 'include' está importado

urlpatterns = [
    # O caminho para o painel de administração
    path('admin/', admin.site.urls),
    
    # Esta é a linha que estava faltando ou incorreta.
    # Ela diz ao Django para enviar qualquer outra URL
    # para ser processada pelo arquivo 'urls.py' da nossa aplicação 'portal'.
    path('', include('portal.urls')),
]