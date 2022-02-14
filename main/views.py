import json
from datetime import datetime
import random
from django.shortcuts import render ,redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import *
from .models import *
import telebot
# Create your views here.
TOKEN = ''
bot = telebot.TeleBot(TOKEN)
user = "801531808"
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
    post = Post.objects.filter(tag=tag)
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

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
            return redirect(f'/post/{slug}') 
    else:
        form = CommentForm()
    context = {"post":posts, 
                'comment' :comment,
                'form':form
               }
    return render(request, "detail.html",context)

def inline_search(request):
    d = json.loads(request.GET["data"])
    if d != "":
        queryset = list(Post.objects.filter(name__icontains=d).values())
        arr = list(Post.objects.filter(description__icontains=d).values())
    else:
        arr = list()
        queryset = list(Post.objects.all().values())
        queryset = random.sample(queryset, 5)
        
    
    data = {}
    data["object_list"] = queryset
    data['obj_list'] = arr

    return JsonResponse(data)

 
def contact(request):
    if request.GET:
        bot.send_message(user, f"Roboblog \n{request.GET['name']} {request.GET['email']} \n comment: {request.GET['body']}")
        redirect('/contact') 
    return render(request, 'contact.html')