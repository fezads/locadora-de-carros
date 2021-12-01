from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarModelos, name='modelos'),
    path('<int:id>/', views.editarModelo, name='modelos'),
    path('cadastrar/', views.cadastrarModelo),
    path('atualizar/<int:id>', views.atualizarModelo),
    path('deletar/<int:id>', views.deletarModelo),
]