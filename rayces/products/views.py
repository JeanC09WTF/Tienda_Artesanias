from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Producto
from .forms import ReservaForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def reservas (request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_exitosa')
    else:
        form = ReservaForm()
    return render(request, 'reservas.html', {'form': form})


def product_list(request):
    category = request.GET.get('category')
    if category:
        products = Producto.objects.filter(category=category)
    else:
        products = Producto.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)
#{'products': products}

def reserva_exitosa(request):
    return render(request, 'reserva_exitosa.html')

def ubicacion (request):
    return render(request, 'ubicacion.html')

def acerca (request):
    return render(request, 'acerca.html')


def product_catalog(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/catalog.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.exclude(id=product_id).order_by('?')[:4] #sugerencias aleatorias
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)


def decoracion_prod(request):
    productos = ['producto1', 'producto2', 'producto3']  # Podría ser una lista, queryset, etc.
    context = {'productos': productos}  # Crear un diccionario de contexto
    return render(request, 'products/decoracion.html', context)


def ropa_pro(request):
    return render(request, 'products/ropa.html')
