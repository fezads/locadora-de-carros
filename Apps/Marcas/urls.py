from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarMarcas),
    path('cadastrar/', views.cadastrarMarca),
    path('<id>/', views.editarMarca),
    path('atualizar/<int:id>', views.atualizarMarca),
    path('deletar/<int:id>', views.deletarMarca),
]