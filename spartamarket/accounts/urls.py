from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("profile/modify/", views.modify, name="modify"),
    path("change-password/", views.change_password, name="change_password"),
    path("delete/", views.delete, name="delete"),
    path("<str:username>/", views.profile, name = "profile"),
    path('profile/update/', views.profile_update, name='profile_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)