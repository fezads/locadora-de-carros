from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import Carro
from Apps.Modelos import models as modelo_models

# Create your views here.

# Abre a tela de lista de carros
def listarCarros(request):
    listaDeCarros = Carro.objects.all()
    listaDeModelos = modelo_models.Modelo.objects.all()

    return render(request, 'carros/index.html', {'carros': listaDeCarros, 'modelos': listaDeModelos})

# Salva a carro no banco de dados
# e redireciona para a lista de carros
def cadastrarCarro(request):
    try:
        placa=request.POST['placa']
        modelo=request.POST['modelo']
        ano=request.POST['ano']
        cor=request.POST['cor']
        descricao=request.POST['descricao']
        observacoes=request.POST['observacoes']

        modelo = modelo_models.Modelo.objects.get(id=modelo)

        Carro.objects.create(
            placa=placa,
            modelo=modelo,
            ano=ano,
            cor=cor,
            descricao=descricao,
            observacoes=observacoes
        )

        messages.success(request, 'Carro cadastrado com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/carros')

# Abre a tela de edição com os dados da carro selecionada
def editarCarro(request, id):
    carro = Carro.objects.get(id=id)
    listaDeCarros = Carro.objects.all()
    listaDeModelos = modelo_models.Modelo.objects.all()

    return render(request, 'carros/index.html', {
        'carro': carro,
        'carros': listaDeCarros,
        'modelos': listaDeModelos
    })

# Atualiza os dados da carro no banco de dados
# e redireciona para a lista de carros
def atualizarCarro(request, id):
    try:
        placa = request.POST['placa']
        modelo = request.POST['modelo']
        ano = request.POST['ano']
        cor = request.POST['cor']
        descricao = request.POST['descricao']
        observacoes = request.POST['observacoes']

        modelo = modelo_models.Modelo.objects.get(id=modelo)
        
        carro = Carro.objects.get(id=id)
        carro.placa = placa
        carro.modelo = modelo
        carro.ano = ano
        carro.cor = cor
        carro.observacoes = observacoes
        carro.descricao = descricao
        carro.save()

        messages.success(request, 'Carro atualizado com sucesso!')
    except:
            messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/carros')

# Deleta a carro do banco de dados
def deletarCarro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()

        messages.success(request, 'Carro removido com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/carros')