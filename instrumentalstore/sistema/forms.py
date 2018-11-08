from django import forms

# Formularios
class FormContacto(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length = 20, widget = forms.TextInput(attrs = { "placeholder": "Ingrese nombre" }))
    correo = forms.EmailField(label = "Correo electróncio", max_length = 30, widget = forms.EmailInput(attrs = { "placeholder": "direccion@correo.com" }))
    mensaje = forms.CharField(label = "Mensaje", widget = forms.Textarea(attrs = { "placeholder": "Ingrese mensaje" }))

class FormCliente(forms.Form):
    runCliente = forms.CharField(label = "RUN cliente", max_length = 10, widget = forms.TextInput(attrs = { "placeholder": "12345678-9" }))
    nombres = forms.CharField(label = "Nombres", max_length = 20, widget = forms.TextInput(attrs = { "placeholder": "Ingrese nombres" }))
    apPaterno = forms.CharField(label = "Apellido paterno", max_length = 20, widget = forms.TextInput(attrs = { "placeholder": "Ingrese apellido paterno"}))
    apMaterno = forms.CharField(label = "Apellido materno", max_length = 20, widget = forms.TextInput(attrs = { "placeholder": "Ingrese apellido materno"}))

class FormInstrumento(forms.Form):
    marca = forms.CharField(label = "Marca", max_length = 20, widget = forms.TextInput(attrs = { "placeholder": "Ingrese marca" }))
    modelo = forms.CharField(label = "Modelo", max_length = 20, widget = forms.TextInput(attrs = { "placeholder": "Ingrese modelo" }))
    serie = forms.CharField(label = "Serie", max_length = 15, widget = forms.TextInput(attrs = { "placeholder": "Ingrese serie" }))
    tipo = forms.CharField(label = "Tipo", max_length = 20, widget = forms.TextInput(attrs = { "placeholder": "Ingrese tipo" }))
    descripcion = forms.CharField(label = "Descripcion", widget = forms.Textarea(attrs = { "placeholder": "Ingrese descripción" }))
    precio = forms.IntegerField(label = "Precio", widget = forms.NumberInput(attrs = { "min": "0" }))
    stock = forms.IntegerField(label = "Stock", widget = forms.NumberInput(attrs = { "min": "0" }))

class Login(forms.Form):
    username = forms.CharField(label = "Nombre de usuario", max_length = 30, widget = forms.TextInput(attrs = { "placeholder": "Ingrese nombre de usuario" }))
    password = forms.CharField(label = "Contraseña", max_length = 30, widget = forms.PasswordInput(attrs = { "placeholder": "Ingrese contraseña" }))
