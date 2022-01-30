from unicodedata import category
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Tag(models.Model):
    name = models.CharField('category', max_length=25)
    slug = models.SlugField('*')

    def __str__(self):
        return self.slug

class Blog(models.Model):
    title = models.CharField('Title:', max_length=25)
    slug = models.SlugField('*',max_length=25)
    post = models.TextField()
    image = models.ImageField("Post image", upload_to='post/')
    tag = models.ForeignKey(Tag, on_delete=CASCADE)
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title