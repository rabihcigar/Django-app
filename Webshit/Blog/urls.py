from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='Blog-Homepage'),
    path('about/', views.about, name='Blog-about'),
]