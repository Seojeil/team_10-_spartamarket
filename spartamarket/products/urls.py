from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
