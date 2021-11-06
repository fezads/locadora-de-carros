from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarClientes),
    path('cadastrar/', views.cadastrarCliente),
    path('<id>/', views.editarCliente),
    path('atualizar/<int:id>', views.atualizarCliente),
    path('deletar/<int:id>', views.deletarCliente),
]