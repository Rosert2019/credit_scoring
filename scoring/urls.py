from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('single_form/', views.single_view, name='single_view'),
    path('file_form/', views.file_view, name='file_view'),
]