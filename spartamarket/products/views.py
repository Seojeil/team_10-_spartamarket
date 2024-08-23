from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.views.decorators.http import require_POST
from .models import Product
from .forms import ProductForm
from django.contrib.auth import logout as auth_logout


def index(request):
    products = Product.objects.all().order_by('-created_at')
    context = {
        'products': products,
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
        'form': form
    }
    return render(request, 'products/create.html', context)


def details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/details.html', context)


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
        'product': product,
        'form': form,
    }
    return render(request, 'products/update.html', context)


@require_POST  # 이 뷰는 POST 요청만 허용
def delete(request):
    if request.user.is_authenticated:  # 사용자가 인증된 상태일 경우
        request.user.delete()  # 사용자 계정 삭제
        auth_logout(request)  # 로그아웃 처리
    return redirect("index")  # 'index' URL로 돌아가기
