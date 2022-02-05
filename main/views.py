import json
from datetime import datetime
from operator import pos
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import *
# Create your views here.
def homeView(request):
    # bot.sendMessage(grID , "Qale")
    posts = Post.objects.select_related("tag").all()
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html",{"page_obj":page_obj,})

def detailView(request, slug):
    posts = Post.objects.select_related("tag").get(slug=slug)
    comments = Comment.objects.filter(post =posts)
    return render(request, 'detail.html', {'post': posts, 'comment':comments})
   

def categoryView(request, slug):
    tag = Tag.objects.get(slug=slug)
    post = Post.objects.filter(tag= tag)
    return render(request, 'index.html', {'posts': post})

def postDetail(request, slug):
    posts = Post.objects.get(slug=slug)
    comment = list(Comment.objects.filter(post= posts))
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.post = posts
            print(f)
            f.save()
    else:
        form = CommentForm()
    context = {"post":posts, 
                'comment' :comment,
                'form':form
               }
    return render(request, "detail.html",context)

def inline_search(request):
    d = json.loads(request.GET["data"])
    queryset = list(Post.objects.filter(name__icontains=d).values())
    data = {}
    data["object_list"] = queryset

    return JsonResponse(data)
