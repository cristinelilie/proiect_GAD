from django.urls import path, include
from . import views

urlpatterns = [
    path('my-login/', views.my_login, name='my-login'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/<id>', views.detail, name='detail'),
    path('delete/<id>', views.delete, name='delete'),
    path('cumpara/<id>', views.change_status, name='change_status'),
    path('update/<id>', views.update, name='update'),
]
