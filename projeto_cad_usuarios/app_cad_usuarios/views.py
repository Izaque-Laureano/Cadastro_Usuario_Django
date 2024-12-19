from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')


def usuarios(request):
    #Salvou os dados da tela no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome') 
    novo_usuario.idade = request.POST.get('idade') 
    novo_usuario.save()
    #Exibe todas as informações que tem no Banco de dados
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    #Retornar os dados para a página de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)
