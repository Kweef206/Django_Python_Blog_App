from django.urls import path
from . import views

urlpatterns = [
    #    homepage, views.home is function from views module that return http response, name is for path
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]