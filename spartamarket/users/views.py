from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET","POST"]) 
def profile(request, username):
    context = {
        "username": username,
    }
    return render(request, "users/profile.html", context)


def product(request, username):
    context = {
        "username":username,
    }
    return render(request, "product/profile.html", context)




