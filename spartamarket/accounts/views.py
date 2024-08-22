from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import SignUpForm

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

