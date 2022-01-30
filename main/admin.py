from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug':('title',)}