from django.shortcuts import render, redirect
from .models import Modelo
from Apps.Marcas import models as marca_models

# Create your views here.

# Abre a tela de lista de modelos
def listarModelos(request):
    listaDeModelos = Modelo.objects.all()
    listaDeMarcas = marca_models.Marca.objects.all()

    return render(request, 'modelos/index.html', {'modelos': listaDeModelos, 'marcas': listaDeMarcas})

# Salva a modelo no banco de dados
# e redireciona para a lista de modelos
def cadastrarModelo(request):
    nome=request.POST['nome']
    marca=request.POST['marca']
    descricao=request.POST['descricao']

    marca = marca_models.Marca.objects.get(id=marca)

    Modelo.objects.create(nome=nome, marca=marca, descricao=descricao)

    return redirect('/modelos')

# Abre a tela de edição com os dados da modelo selecionada
def editarModelo(request, id):
    modelo = Modelo.objects.get(id=id)
    listaDeModelos = Modelo.objects.all()
    listaDeMarcas = marca_models.Marca.objects.all()

    return render(request, 'modelos/index.html', {'modelo': modelo, 'modelos': listaDeModelos, 'marcas': listaDeMarcas})

# Atualiza os dados da modelo no banco de dados
# e redireciona para a lista de modelos
def atualizarModelo(request, id):
    nome = request.POST['nome']
    marca = request.POST['marca']
    descricao = request.POST['descricao']

    marca = marca_models.Marca.objects.get(id=marca)
    
    modelo = Modelo.objects.get(id=id)
    modelo.nome = nome
    modelo.marca = marca
    modelo.descricao = descricao
    modelo.save()

    return redirect('/modelos')

# Deleta a modelo do banco de dados
def deletarModelo(request, id):
    modelo = Modelo.objects.get(id=id)
    modelo.delete()

    return redirect('/modelos')