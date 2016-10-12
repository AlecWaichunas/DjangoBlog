from django.shortcuts import render
from App.models import Blog

# Create your views here.
def index_view(request):
    context = {
        'site_name': 'Alec\'s blog',
        'blogs': Blog.objects.all()
    }
    return render(request, 'index.html', context)
