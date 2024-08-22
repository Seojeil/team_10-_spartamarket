from django.shortcuts import(
    render,
    redirect,
    get_object_or_404,
    )
from django.views.decorators.http import require_POST
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all().order_by('-created_at')
    context = {
        'products':products,
    }
    return render(request, 'products/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('products:details', product.pk)
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, 'products/create.html', context)


def details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product':product,
    }
    return render(request, 'products/details.html', context)


@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
                product = form.save()
                return redirect("products:details", product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        'product':product,
        'form':form,
    }
    return render(request, 'products/update.html', context)


def comments(request, pk):
    product = get_object_or_404(Product, pk=pk)
    pass

