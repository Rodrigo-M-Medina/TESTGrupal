from django.urls import path
from App1.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('registrar/', registrar, name="registrar"),
    path('iniciar/', ingresar, name="ingresar"),
    path('bienvenido/', bienvenido, name="bienvenido"),
    path("desconectarse/", desconectarse, name = "desconectarse" ),
    path("editarusuario/", editarUsuario, name = "Editar_Usuario" ),
    path("usuariosregistrados/", usuariosRegistrados, name = "Usuarios_Registrados"),
    path("eliminarusuarios/<pk>", eliminarUsuario, name = "Eliminar_Usuarios"), 
]