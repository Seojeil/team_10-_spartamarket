from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import logout as auth_logout



# @require_http_methods(["GET","POST"]) 
# def users(request):
#     return render(request, "users/users.html")


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




