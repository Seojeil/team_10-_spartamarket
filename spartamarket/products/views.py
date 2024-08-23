from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.views.decorators.http import (
    require_POST,
    require_http_methods
)
from django.contrib.auth.decorators import login_required
from .models import Product, Comment
from .forms import ProductForm, CommentForm


def index(request):
    products = Product.objects.all().order_by('-created_at')
    context = {
        'products': products,
    }
    return render(request, 'products/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('products:details', product.pk)
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/create.html', context)


def details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.hits += 1
    product.save()
    comments = product.comments.all()
    comment_form = CommentForm()
    context = {
        'product': product,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'products/details.html', context)


@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.author:
        product.delete()
        return redirect('index')
    else:
        return redirect('articles:details', product.pk)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.author:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                product = form.save()
                return redirect("products:details", product.pk)
        else:
            form = ProductForm(instance=product)

        context = {
            'product': product,
            'form': form,
        }
        return render(request, 'products/update.html', context)
    else:
        return redirect('articles:details', product.pk)


@login_required
def comments(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.author = request.user
        comment.save()
        return redirect("products:details", product.pk)


@require_POST
def comments_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product_pk = comment.product.pk
    if request.user == comment.author:
        comment.delete()
    return redirect("products:details", pk=product_pk)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
            product.save()
        return redirect('products:details', pk=pk)
    return redirect('accounts:login')
