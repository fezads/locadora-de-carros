from django.shortcuts import render, redirect
from django.contrib import messages
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
    try:
        nome=request.POST['nome']
        marca=request.POST['marca']
        descricao=request.POST['descricao']

        marca = marca_models.Marca.objects.get(id=marca)

        Modelo.objects.create(
            nome=nome,
            marca=marca,
            descricao=descricao
        )

        messages.success(request, 'Modelo cadastrado com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/modelos')

# Abre a tela de edição com os dados da modelo selecionada
def editarModelo(request, id):
    modelo = Modelo.objects.get(id=id)
    listaDeModelos = Modelo.objects.all()
    listaDeMarcas = marca_models.Marca.objects.all()

    return render(request, 'modelos/index.html', {
        'modelo': modelo,
        'modelos': listaDeModelos,
        'marcas': listaDeMarcas
    })

# Atualiza os dados da modelo no banco de dados
# e redireciona para a lista de modelos
def atualizarModelo(request, id):
    try:
        nome = request.POST['nome']
        marca = request.POST['marca']
        descricao = request.POST['descricao']

        marca = marca_models.Marca.objects.get(id=marca)
        
        modelo = Modelo.objects.get(id=id)
        modelo.nome = nome
        modelo.marca = marca
        modelo.descricao = descricao
        modelo.save()

        messages.success(request, 'Modelo atualizado com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/modelos')

# Deleta a modelo do banco de dados
def deletarModelo(request, id):
    try:
        modelo = Modelo.objects.get(id=id)
        modelo.delete()

        messages.success(request, 'Modelo removido com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/modelos')