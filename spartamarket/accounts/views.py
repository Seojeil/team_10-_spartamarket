from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm


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
