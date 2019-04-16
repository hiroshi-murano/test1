from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_input/', views.data_input, name='data_input'),
    path('api_01/', views.api_01, name='api_01'),
]