from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarClientes, name='clientes'),
    path('<int:id>/', views.editarCliente, name='clientes'),
    path('cadastrar/', views.cadastrarCliente),
    path('atualizar/<int:id>', views.atualizarCliente),
    path('deletar/<int:id>', views.deletarCliente),
]