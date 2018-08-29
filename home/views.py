from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *

# Create your views here.
def view_home(request):
    return render(request, 'home.html')

def view_nosotros(request):
    return render(request, 'nosotros.html')

def view_ingresar(request):
    return render(request, 'ingresar.html')

def view_contacto(request):
    info_enviada = False
    email = ''
    title = ''
    text  = ''

    if request.method == 'POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            info_enviada = True
            email = formulario.cleaned_data['correo']
            title = formulario.cleaned_data['titulo']
            text = formulario.cleaned_data['texto']
        
    else:
        formulario = contacto_form()

    return render(request, 'contacto.html', locals())

def view_productos  (request):
    lista = Producto.objects.filter()
    return render(request, 'productos.html', locals())

def view_add_producto (request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            formulario = add_producto_form(request.POST, request.FILES)
            
            if formulario.is_valid():
                formulario.save()
                return redirect('/productos')
            else:
                msg = 'El Formulario contiene datos no validos'

        else:    
            formulario = add_producto_form()
        
        return render(request, 'add_producto.html', locals())
    
    else:
        return redirect('/login/')

def view_ver_producto(request, id_prod):
    try: 
        producto = Producto.objects.get(id = id_prod)
    except:
        print ("Error en la consulta el producto no existe")
        msg = "Error en la consulta el producto no existe"
    return render(request, 'ver_producto.html', locals())

def view_editar_producto(request, id_prod):
    producto = Producto.objects.get(id = id_prod)

    if request.method == 'POST':
        formulario = add_producto_form(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('ver_producto', id_prod = id_prod)

    else:
        formulario = add_producto_form(instance=producto)
    return render(request, 'add_producto.html', locals())

def view_eliminar_producto(request, id_prod):
    producto = Producto.objects.get(id = id_prod)
    producto.delete()

    return redirect('/productos/')

def view_categorias (request):
    categorias = Categoria.objects.filter()
    return render(request, 'categorias.html', locals())

def view_add_categoria (request):
    if request.method == 'POST':
        formulario = add_categoria_form(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('/categorias')
        else:
            msg = 'El formulario contiene datos no validos.'
    
    else:
        formulario = add_categoria_form()

    return render(request, 'add_categoria.html', locals())

def view_marcas (request):
    marcas = Marca.objects.filter();
    return render(request, 'marcas.html', locals())

def view_add_marca (request):
    if request.method == 'POST':
        formulario = add_marca_form(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('/marcas')
        else:
            msg = 'El formulario contiene datos no validos.'
    
    else:
        formulario = add_marca_form()

    return render(request, 'add_marca.html', locals())

def view_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            formulario = login_form(request.POST)
            if formulario.is_valid():
                usuario_form = formulario.cleaned_data['usuario']
                clave_form = formulario.cleaned_data['clave']

                usuario = authenticate(username = usuario_form, password = clave_form)

                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return redirect('/')
                else:
                    msg = 'Información: Usuario o clave incorrectos'
        else:
            formulario = login_form()

        return render(request, 'login.html', locals())

def view_logout(request):
    logout(request)
    return redirect('/login/')

def view_registrar_usuario(request):
    formulario = register_form()

    if request.method == 'POST':
        formulario = register_form(request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            correo = formulario.cleaned_data['email']
            password1 = formulario.cleaned_data['password1']
            password2 = formulario.cleaned_data['password2']

            u = User.objects.create_user(username = usuario, email = correo, password = password1)
            u.save()

            return render(request, 'thanks_register.html', locals())
        else:
            return render(request, 'registrar_usuario.html', locals())
            
    return render(request, 'registrar_usuario.html', locals())