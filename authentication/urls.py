from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home),
    path("signup/", views.signup),
    path("login/", views.login),
    path("logout/", views.logout),
]
