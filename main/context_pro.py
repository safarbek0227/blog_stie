from .models import *

def view_all(request):
    context = {
        "tag":Tag.objects.all(),
    }
    return context 