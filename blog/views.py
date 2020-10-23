from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import posts, Cat_org

# Create your views here.
class index(ListView):
    model = posts
    template_name = "blog/index.html"