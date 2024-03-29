from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Post)
class productAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

	
admin.site.register(Comment)