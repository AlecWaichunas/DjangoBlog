from django.shortcuts import get_object_or_404, render
from App.models import Blog

# Create your views here.
def index_view(request):
    context = {
        'site_name': 'Alec\'s blog',
        'blogs': Blog.objects.all().order_by("-blog_date")
    }
    return render(request, 'index.html', context)

def blog_view(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog.html', context)
