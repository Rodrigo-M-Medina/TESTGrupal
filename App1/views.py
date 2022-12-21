from django.shortcuts import render
#-------------- imports de funciones de django ----------
from django.contrib.auth import login, authenticate, logout
#--------------- imports de forms creados en forms.py -----------
from App1.forms import CrearUsuario, UserEditForm
#--------------- imports de forms existentes en django ------------
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User




#----------- Pagina de inicio ----------------

def inicio(request):
    return render (request, "inicio.html")

def bienvenido(request):
    return render (request, "bienvenido.html")




#---------- Registrar Usuario --------------

def ingresar(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombreusuario = form.cleaned_data.get("username")
            claveusuario = form.cleaned_data.get("password")
            usuario = authenticate (username=nombreusuario, password=claveusuario)
            if usuario is not None:
                login(request, usuario)
                return render (request, "bienvenido.html")
            else:
                return render (request, "ingresar.html", {"form":form})
        else:
            return render (request, "ingresar.html",{"form":form})
    else:
        form=AuthenticationForm()
    
    return render (request, "ingresar.html",{"form":form})



#----------- inicio de sesion --------------


def registrar(request):
    if request.method=="POST":
        form=CrearUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "inicio.html")
    else:
        form = CrearUsuario()
    return render(request, 'registrar.html',{"form":form})


#----------- Cerrar Sesion -------------------

def desconectarse(request):
    logout(request)
    return render(request, "inicio.html")


#------------ mostrar usuarios --------------

def usuariosRegistrados(request):
    usuarios = User.objects.all()
    return render(request, "usuarios_registrados.html", {"usuarios":usuarios} )


#------------- eliminar usuarios ---------

def eliminarUsuario(request, pk):
    usuario = User.objects.filter(id=pk)
    usuario.delete()
    usuarios=User.objects.all()
    return usuariosRegistrados(request)


#-------------- editar Usuario ------------- 

def editarUsuario(request, id):
    usuario = User.objects.get(id=id)

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():

            info = formulario.cleaned_data
            usuario.username = info['username']
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']

            usuario.save()
            return render(request, "usuarios_registrados.html")
    else:
        formulario = UserEditForm(initial={"username":usuario.username, "email":usuario.email, "password1":usuario.password1, "password2":usuario.password2})
    return render(request, "editar_perfil.html", {"Formulario": formulario})

