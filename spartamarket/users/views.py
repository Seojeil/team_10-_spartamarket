from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm  # 사용자 생성 및 변경 폼을 위한 Django 폼 임포트
from .forms import CustomUserChangeForm, CustomUserCreationForm



@require_http_methods(["GET","POST"]) 
def users(request):
    return render(request, "users/users.html")


@require_http_methods(["GET","POST"]) 
def profile(request, username):
    context = {
        "username": username,
    }
    return render(request, "users/profile.html", context)

def good(request):
    pass


def product(request, username):
    context = {
        "username":username,
    }
    return render(request, "product/profile.html", context)


@require_POST  # 이 뷰는 POST 요청만 허용
def logout(request):
    if request.user.is_authenticated:  # 사용자가 인증된 상태일 경우
        auth_logout(request)  # 사용자를 로그아웃 처리
    return redirect("index")  # 'index' URL로 돌아가기


@require_http_methods(["GET", "POST"])  # 이 뷰는 GET과 POST 요청만 허용
def modify(request, username):
    if request.method == "POST":  # 요청이 POST일 경우 (사용자가 업데이트 폼을 제출했을 때)
        form = CustomUserChangeForm(request.POST, instance=request.user)  # 제출된 데이터를 바탕으로 폼 인스턴스 생성
        if form.is_valid():  # 폼이 유효한 경우
            form.save()  # 사용자 정보를 업데이트
            return redirect("index")  # 'index' URL로 리디렉션
    else:
        form = CustomUserChangeForm(instance=request.user)  # GET 요청일 경우, 현재 사용자 데이터를 바탕으로 폼 생성
    context = {"form": form}  # 템플릿에 전달할 컨텍스트 생성
    return render(request, "accounts/update.html", context)  # 'accounts/update.html' 템플릿을 렌더링



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



