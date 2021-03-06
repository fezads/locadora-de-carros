from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente

# Create your views here.

# Abre a tela de lista de clientes
def listarClientes(request):
    listaDeClientes = Cliente.objects.all()

    return render(request, 'clientes/index.html', {'clientes': listaDeClientes})

# Salva a cliente no banco de dados
# e redireciona para a lista de clientes
def cadastrarCliente(request):
    try:
        nome=request.POST['nome']
        cpf=request.POST['cpf']
        email=request.POST['email']
        telefone=request.POST['telefone']

        Cliente.objects.create(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone
        )

        messages.success(request, 'Cliente cadastrado com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/clientes')

# Abre a tela de edição com os dados da cliente selecionada
def editarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    listaDeClientes = Cliente.objects.all()

    return render(request, 'clientes/index.html', {
        'cliente': cliente,
        'clientes': listaDeClientes
    })

# Atualiza os dados da cliente no banco de dados
# e redireciona para a lista de clientes
def atualizarCliente(request, id):
    try:
        nome=request.POST['nome']
        cpf=request.POST['cpf']
        email=request.POST['email']
        telefone=request.POST['telefone']

        cliente = Cliente.objects.get(id=id)
        cliente.nome = nome
        cliente.cpf = cpf
        cliente.email = email
        cliente.telefone = telefone
        cliente.save()

        messages.success(request, 'Cliente atualizado com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/clientes')

# Deleta a cliente do banco de dados
def deletarCliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()

        messages.success(request, 'Cliente removido com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/clientes')