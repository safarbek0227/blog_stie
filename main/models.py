from ast import Delete
from aiohttp import request
from django.db import models
from django.db import models
from django.shortcuts import reverse
# from accounts.models import Profile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Tag(models.Model):
    name = models.CharField('categoriya nomi', max_length=25)
    slug = models.SlugField('*', max_length=25)

    class Meta:
        ordering = ["id"]
    def __str__(self):
        return self.name
    
class Post(models.Model):
    name = models.CharField('title', max_length=80)
    slug = models.SlugField('*', max_length=50)
    image = models.ImageField("Blog image", upload_to='product_images/')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    description = RichTextField("About product")
    like = models.PositiveIntegerField('like', default=0)
    view = models.PositiveIntegerField('views', default=0)
    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post ,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
