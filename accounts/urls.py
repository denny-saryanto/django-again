from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_render, name="login"),
    path('logout/', views.logout_render, name="logout"),
    path('register/', views.register_render, name="register"),
]
