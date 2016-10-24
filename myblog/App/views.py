from django.shortcuts import get_object_or_404, render
from App.models import Blog, Comment

import datetime

# Create your views here.
def index_view(request):
    context = {
        'site_name': 'Alec\'s blog',
        'blogs': Blog.objects.all().order_by("-blog_date")
    }
    return render(request, 'index.html', context)

def blog_view(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        comment_name = "Alec Waichunas"
        comment_text = request.POST.get('comment', '')
        comment = Comment(comment_author=comment_name, comment_text=comment_text, comment_date=datetime.datetime.today(), blog=blog)
        comment.save()
    comments = Comment.objects.all().filter(blog=blog)
    if comments is None:
        comments = {}

    print(comments)
    context = {
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'blog.html', context)
