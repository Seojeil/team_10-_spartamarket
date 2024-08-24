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
from .models import Product, Comment, HashTag
from .forms import ProductForm, CommentForm
from django.db.models import Count

# 제품 포스트 정렬 
def index(request):
    sort = request.GET.get('sort', 'date')  # 디폴트 날짜로 정렬 
    if sort == 'likes':
        products = Product.objects.annotate(like_count=Count('like_users')).order_by('-like_count', '-created_at') #찜 정렬
    elif sort == 'comments':
        products = Product.objects.annotate(comment_count=Count('comments')).order_by('-comment_count', '-created_at') # 댓글 정렬
    else:  
        products = Product.objects.all().order_by('-created_at') # 날짜 정렬

    context = {
        'products': products,
    }
    return render(request, 'products/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        hashtags = request.POST.get('hashtags')
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            if hashtags:
                create_hashtag(hashtags, product)
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
    hashtags = product.hashtags.all()
    comments = product.comments.all()
    comment_form = CommentForm()
    context = {
        'product': product,
        'comments': comments,
        'comment_form': comment_form,
        'hashtags': hashtags,
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
    current_hashtags = product.hashtags.all()
    if request.user == product.author:
        if request.method == 'POST':
            product.hashtags.clear()
            form = ProductForm(request.POST, request.FILES, instance=product)
            hashtags = request.POST.get('hashtags')
            if form.is_valid():
                product = form.save()
                if hashtags:
                    create_hashtag(hashtags, product)
                return redirect("products:details", product.pk)
        else:
            form = ProductForm(instance=product)

        context = {
            'product': product,
            'current_hashtags': current_hashtags,
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

def create_hashtag(hashtags, product):
    hashtags = hashtags.split(',')
    for name in hashtags:
        if name != '':
            hashtag, created = HashTag.objects.get_or_create(name=name)
            product.hashtags.add(hashtag)
        product.save()