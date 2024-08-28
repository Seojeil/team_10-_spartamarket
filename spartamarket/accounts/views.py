from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import (
    require_http_methods,
    require_POST
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
    get_user_model,
)
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import SignUpForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import user_passes_test
from .forms import ProfileUpdateForm

def not_logged_in(user):
    return not user.is_authenticated


# 로그인
@user_passes_test(not_logged_in, login_url='index')
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next') or "index"
            if next_url == '/accounts/login/':
                next_url = "index"
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('index')

# 회원가입
@user_passes_test(not_logged_in, login_url='index')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    context = {
        "form": form
    }
    return render(request, "accounts/signup.html", context)


# 프로필 화면 구성
@login_required
@require_http_methods(["GET", "POST"])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    selected_option = request.GET.get("product_option")    
    if selected_option == 'all':
        products = Product.objects.filter(author=user).order_by('-created_at')
    else:
        products = Product.objects.filter(
            like_users=user).order_by('-created_at')
        
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', username=user.username)  
    else:
        form = ProfileUpdateForm(instance=user)
        
    context = {
        "user": user,
        'products': products,
        'option': selected_option,  
        'form': form,
    }
    
    return render(request, "accounts/profile.html", context)


# 사용자 정보수정
@require_http_methods(["GET", "POST"])  
def modify(request):
    if request.method == "POST":  
        form = CustomUserChangeForm(request.POST, instance=request.user)  
        image_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user) 
        if form.is_valid(): 
            form.save() 
            image_form.save()  
            return redirect("accounts:profile", username=request.user.username)  
    else:
        form = CustomUserChangeForm(instance=request.user) 
        image_form = ProfileUpdateForm(instance=request.user) 
    context = {
        "form": form,
        "image_form":image_form
        } 
    return render(request, "accounts/modify.html", context)  


# 비밀번호 변경 기능
@require_http_methods(["GET", "POST"])  # 이 뷰는 GET과 POST 요청만 허용
def change_password(request):
    if request.method == "POST":  # 요청이 POST일 경우 (사용자가 비밀번호 변경 폼을 제출했을 때)
        # 제출된 데이터를 바탕으로 폼 인스턴스 생성
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():  # 폼이 유효한 경우
            form.save()  # 비밀번호를 변경
            # 세션의 인증 정보를 업데이트하여 로그아웃 방지
            update_session_auth_hash(request, form.user)
            return redirect("index")  # 'index' URL로 리디렉션
    else:
        form = PasswordChangeForm(request.user)  # GET 요청일 경우 빈 폼 인스턴스 생성
    context = {
        'form': form
    }  # 템플릿에 전달할 컨텍스트 생성
    # 'accounts/change_password.html' 템플릿을 렌더링
    return render(request, "accounts/change_password.html", context)


# 회원탈퇴 기능
@require_POST 
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()  
        auth_logout(request) 
    return redirect("index") 


# 팔로우 기능
@require_http_methods(["GET", "POST"])
def follow(request, username):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), username=username)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')






