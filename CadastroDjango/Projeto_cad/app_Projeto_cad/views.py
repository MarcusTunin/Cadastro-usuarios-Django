from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Exibir usuarios em nova pagina
    usuarios= {
        'usuarios': Usuario.objects.all()
    }

    # Retornar usuarios para a pag de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)