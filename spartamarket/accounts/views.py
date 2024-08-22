from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import SignUpForm,CustomUserChangeForm
from django.contrib.auth.forms import  PasswordChangeForm  
from django.contrib.auth import update_session_auth_hash


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # next_url = request.GET("next") or "index"
            return redirect('index')
        
    else:
        form = AuthenticationForm()
        
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
        else:
            # 폼 오류 메시지를 콘솔에 출력
            print(form.errors)
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@require_http_methods(["GET", "POST"])  # 이 뷰는 GET과 POST 요청만 허용
def modify(request):
    if request.method == "POST":  # 요청이 POST일 경우 (사용자가 업데이트 폼을 제출했을 때)
        form = CustomUserChangeForm(request.POST, instance=request.user)  # 제출된 데이터를 바탕으로 폼 인스턴스 생성
        if form.is_valid():  # 폼이 유효한 경우
            form.save()  # 사용자 정보를 업데이트
            return redirect("index")  # 'index' URL로 리디렉션
    else:
        form = CustomUserChangeForm(instance=request.user)  # GET 요청일 경우, 현재 사용자 데이터를 바탕으로 폼 생성
    context = {"form": form}  # 템플릿에 전달할 컨텍스트 생성
    return render(request, "accounts/modify.html", context)  # 'accounts/update.html' 템플릿을 렌더링



def change_password(request):
    if request.method == "POST":  # 요청이 POST일 경우 (사용자가 비밀번호 변경 폼을 제출했을 때)
        form = PasswordChangeForm(request.user, request.POST)  # 제출된 데이터를 바탕으로 폼 인스턴스 생성
        if form.is_valid():  # 폼이 유효한 경우
            form.save()  # 비밀번호를 변경
            update_session_auth_hash(request, form.user)  # 세션의 인증 정보를 업데이트하여 로그아웃 방지
            return redirect("index")  # 'index' URL로 리디렉션
    else:
        form = PasswordChangeForm(request.user)  # GET 요청일 경우 빈 폼 인스턴스 생성
    context = {'form':form}  # 템플릿에 전달할 컨텍스트 생성
    return render(request, "accounts/change_password.html", context)  # 'accounts/change_password.html' 템플릿을 렌더링
