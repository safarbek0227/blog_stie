from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class HomeView(ListView):
    model = Blog
    template_name = 'index.html' 
    context_object_name = "Blog"  
    paginate_by = 4

def PostView(request, slug):
    Post = Blog.objects.get(slug=slug)
    return render(request, 'detail.html', {'Post': Post, })

def TagView(request, slug):
    print(slug)
    tag = Tag.objects.get(slug=slug)
    blog = Blog.objects.filter(tag=tag)
    return render(request, 'index.html', {"Blog": blog})
