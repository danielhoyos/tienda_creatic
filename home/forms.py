from django import forms
from .models import *
from django.contrib.auth.models import User

class contacto_form(forms.Form):
    correo = forms.EmailField(widget = forms.TextInput(attrs={ 'class' : 'form-control'}))
    titulo = forms.CharField(widget = forms.TextInput(attrs={ 'class' : 'form-control'}))
    texto  = forms.CharField(widget = forms.TextInput(attrs={ 'class' : 'form-control'}))

class add_producto_form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class add_categoria_form(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class add_marca_form (forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class login_form(forms.Form):
    usuario = forms.CharField(widget = forms.TextInput(attrs={'class' : 'form-control' }))
    clave = forms.CharField(widget = forms.PasswordInput(render_value = False, attrs={'class' : 'form-control' }))

class register_form(forms.Form):
    username    = forms.CharField(widget = forms.TextInput(attrs={ 'class' : 'form-control' }))
    email       = forms.EmailField(widget = forms.TextInput(attrs={ 'class' : 'form-control' }))
    password1   = forms.CharField(label = "Password", widget = forms.PasswordInput(attrs={ 'class' : 'form-control' }, render_value = False))
    password2   = forms.CharField(label = "Confirmar Password", widget = forms.PasswordInput(attrs={ 'class' : 'form-control' }, render_value = False))

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            u = User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de Usuario ya registrado')

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            e = User.objects.get(email = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Correo Electronico ya existe')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 == password2:
            pass
        else:
            raise forms.ValidationError('Los password con coinciden')


