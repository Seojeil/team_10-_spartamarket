from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path("", views.users, name = "users"),
    path("profile/<str:username>/", views.profile, name = "profile"),
    path("profile/logout/", views.logout, name="logout"),
    path()
]
