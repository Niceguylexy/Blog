from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('post_detail/<slug:slug>', views.post_detail, name="detail"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.signout, name='logout'),
]