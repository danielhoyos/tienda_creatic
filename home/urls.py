from django.urls import path
from .views import *

urlpatterns = [
    path('', view_home, name="home"),
    path('nosotros/', view_nosotros, name="nosotros"),
    path('contacto/', view_contacto, name="contacto"),
    path('login/', view_login, name="login"),
    path('logout/', view_logout, name="logout"),
    path('registrar_usuario/', view_registrar_usuario, name="registrar_usuario"),

    path('productos/', view_productos, name="productos"),
    path('add_producto/', view_add_producto, name="add_producto"),
    path('ver_producto/<int:id_prod>/', view_ver_producto, name="ver_producto"),
    path('editar_producto/<int:id_prod>/', view_editar_producto, name="editar_producto"),
    path('eliminar_producto/<int:id_prod>/', view_eliminar_producto, name="eliminar_producto"),

    path('categorias/', view_categorias, name="categorias"),
    path('add_categoria/', view_add_categoria, name="add_categoria"),
    
    path('marcas/', view_marcas, name="marcas"),
    path('add_marca/', view_add_marca, name="add_marca"),

]