from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarModelos),
    path('cadastrar/', views.cadastrarModelo),
    path('<id>/', views.editarModelo),
    path('atualizar/<int:id>', views.atualizarModelo),
    path('deletar/<int:id>', views.deletarModelo),
]