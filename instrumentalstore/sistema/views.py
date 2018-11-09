from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import Login, FormCliente, FormInstrumento, FormContacto
from .models import Cliente, Instrumento, Mensaje

# Create your views here.
def index(request):
    return render(request, "index.html", { "titulo": "Inicio" })

def nosotros(request):
    return render(request, "quienes.html", { "titulo": "¿Quiénes somos?" })

def ingresar(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username = data.get("username"), password = data.get("password"))
            if user is not None:
                login(request, user)
                return redirect("index")
    else:
        form = Login()
    return render(request, "login.html", { "titulo": "Inicio de sesión", "form": form })

def contacto(request):
	if request.method == "POST":
		form = FormContacto(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			Mensaje.objects.create(nombreRemitente = data.get("nombre"), correo = data.get("correo"), mensaje = data.get("mensaje"))
			return redirect("contacto")
	else:
		form = FormContacto()
	return render(request, "contacto.html", { "titulo": "Contacto", "form": form })

@login_required(login_url = "login")
@staff_member_required
def gestionClientes(request):
    if request.method == "POST":
        form = FormCliente(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Cliente.objects.create(run = data.get("runCliente"), nombres = data.get("nombres"), apPaterno = data.get("apPaterno"), apMaterno = data.get("apMaterno"))
            return redirect("gestionClientes")
    else:
        form = FormCliente()

    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 5)

    try:
        pag = int(request.GET.get("page", 1))
    except ValueError:
        pag = 1

    try:
        clientes = paginator.page(pag)
    except (InvalidPage, EmptyPage):
        clientes = paginator.page(paginator.num_pages)

    return render(request, "gestionClientes.html", { "titulo": "Gestión de clientes", "listado": clientes, "form": form })

@login_required(login_url = "login")
@staff_member_required
def gestionInstrumentos(request):
    if request.method == "POST":
        form = FormInstrumento(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Instrumento.objects.create(marca = data.get("marca"), modelo = data.get("modelo"), serie = data.get("serie"), tipo = data.get("tipo"), descripcion = data.get("descripcion"), precio = data.get("precio"), stock = data.get("stock"))
            return redirect("gestionInstrumentos")
    else:
        form = FormInstrumento()

    instrumentos = Instrumento.objects.all()
    paginator = Paginator(instrumentos, 5)

    try:
        pag = int(request.GET.get("page", 1))
    except ValueError:
        pag = 1

    try:
        instrumentos = paginator.page(pag)
    except (InvalidPage, EmptyPage):
        instrumentos = paginator.page(paginator.num_pages)

    return render(request, "gestionInstrumentos.html", { "titulo": "Gestión de instrumentos", "listado": instrumentos, "form": form})

@login_required(login_url = "login")
@staff_member_required
def actualizarCliente(request, pk):
    cliente = Cliente.objects.get(codigoCliente = pk)
    if not cliente:
        return render(request, "editarClienteFail.html", { "titulo": "Cliente no existente" })

    if request.method == "POST":
        form = FormCliente(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cliente.run = data.get("runCliente")
            cliente.nombres = data.get("nombres")
            cliente.apPaterno = data.get("apPaterno")
            cliente.apMaterno = data.get("apMaterno")
            cliente.save()
            return redirect("gestionClientes")
    else:
        data = {
            "runCliente": cliente.run,
            "nombres": cliente.nombres,
            "apPaterno": cliente.apPaterno,
            "apMaterno": cliente.apMaterno
        }
        form = FormCliente(data)
    return render(request, "editarCliente.html", { "titulo": "Editando a %s" % cliente.run, "form": form })

@login_required(login_url = "login")
@staff_member_required
def actualizarInstrumento(request, pk):
    instrumento = Instrumento.objects.get(codigoInstrumento = pk)
    if not instrumento:
        return render(request, "editarInstrumentoFail.html", { "titulo": "Instrumento no existente" })

    if request.method == "POST":
        form = FormInstrumento(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            instrumento.marca = data.get("marca")
            instrumento.modelo = data.get("modelo")
            instrumento.serie = data.get("serie")
            instrumento.tipo = data.get("tipo")
            instrumento.descripcion = data.get("descripcion")
            instrumento.precio = data.get("precio")
            instrumento.stock = data.get("stock")
            instrumento.save()
            return redirect("gestionInstrumentos")
    else:
        data = {
            "marca": instrumento.marca,
            "modelo": instrumento.modelo,
            "serie": instrumento.serie,
            "tipo": instrumento.tipo,
            "descripcion": instrumento.descripcion,
            "precio": instrumento.precio,
            "stock": instrumento.stock
        }
        form = FormInstrumento(data)
    return render(request, "editarInstrumento.html", { "titulo": "Editando a instrumento %s" % instrumento.codigoInstrumento, "form": form })

@login_required(login_url = "login")
@staff_member_required
def eliminarCliente(request, pk):
    cliente = Cliente.objects.get(codigoCliente = pk)
    if cliente:
        cliente.delete()
        return redirect("gestionClientes")
    return render(request, "eliminarClienteFail.html", { "titulo": "Error al eliminar cliente" })

@login_required(login_url = "login")
@staff_member_required
def eliminarInstrumento(request, pk):
    instrumento = Instrumento.objects.get(codigoInstrumento = pk)
    if instrumento:
        instrumento.delete()
        return redirect("gestionInstrumentos")
    return render(request, "eliminarInstrumentoFail.html", { "titulo": "Error al eliminar instrumento" })
