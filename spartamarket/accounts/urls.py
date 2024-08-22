from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("<str:username>/", views.profile, name = "profile"),
    path("profile/modify/", views.modify, name="modify"),
    path("change-password/", views.change_password, name="change_password"),
    path("delete/", views.delete, name="delete"),
]
