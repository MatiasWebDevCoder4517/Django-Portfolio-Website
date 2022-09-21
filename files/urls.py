# Import path module
from django.urls import path, include
from files import views


from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ecomm", views.ecomm, name="ecomm"),
    path("student", views.student, name="student"),
    path("instructor", views.instructor, name="instructor"),
    path("bitcoin", views.bitcoin, name="bitcoin"),


]

