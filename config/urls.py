from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a interface de administração do Django
    path('', include('app_calculator.urls')),  # Inclui as rotas do app_calculator
    # Outras rotas de apps podem ser adicionadas aqui da mesma forma:
    # path('outro_app/', include('outro_app.urls')),
]
