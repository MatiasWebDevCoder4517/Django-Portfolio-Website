from django.shortcuts import redirect, render
import os
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse, Http404
from wsgiref.util import FileWrapper
import mimetypes


def home(request):
    return render(request, "index.html")


def ecomm(request):
    return render(request, "ecomm.html")


def student(request):
    return render(request, "student.html")


def instructor(request):
    return render(request, "instructor.html")


def bitcoin(request):
    return render(request, "bitcoin.html")
