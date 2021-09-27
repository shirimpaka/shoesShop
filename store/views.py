from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Shoe

class HomeListView(ListView):
    model = Shoe
    template_name = "home.html"
    context_object_name = 'shoes'