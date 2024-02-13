from django.urls import path
from snippets import views

urlpatterns = [
    path('', views.index),
    path('snippets/<int:pk>/', views.snippet_detail),
]
