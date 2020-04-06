from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    #    homepage, views.home is function from views module that return http response, name is for path
    path('', views.home, name='blog-home'),
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name='blog-about'),
]