import random
from ctypes.wintypes import tagPOINT
from .models import *

def view_all(request):
    products = list(Post.objects.select_related("tag").all())
    products = random.sample(products, 5)
    tags =list(Tag.objects.all())
    tags = random.sample(tags, 5)
    context = {
        'randoms':products,
        'rantags': tags
    }
    return context 