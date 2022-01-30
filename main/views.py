from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class homeView(ListView):
    model = Blog
    template_name = 'index.html' 
    context_object_name = "Blog"  
    paginate_by = 4

def postView(request, slug):
    Post = Blog.objects.get(slug=slug)
    return render(request, 'detail.html', {'Post': Post})
