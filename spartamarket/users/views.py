from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET","POST"])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    context = {
        "user": user,
    }
    return render(request, "users/profile.html", context)