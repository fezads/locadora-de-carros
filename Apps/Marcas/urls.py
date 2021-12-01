from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarMarcas, name='marcas'),
    path('<int:id>/', views.editarMarca, name='marcas'),
    path('cadastrar/', views.cadastrarMarca),
    path('atualizar/<int:id>', views.atualizarMarca),
    path('deletar/<int:id>', views.deletarMarca),
]