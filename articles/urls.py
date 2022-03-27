from django.urls import path
from . import views

urlpatterns = [
    path('', views.searchArticle, name="searchArticle"),
    path('<int:id>/', views.showId, name="showId"),
    path('create/', views.inputArticle, name="createArticle"),
]