from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("profile/modify/<str:username>/", views.modify, name="modify"),
    path("profile/modify/", views.modify, name="modify"),
    path("change-password/", views.change_password, name="change_password"),
]
