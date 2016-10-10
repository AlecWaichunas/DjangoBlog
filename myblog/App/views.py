from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {
        'site_name': 'Alec\'s blog'
    }
    return render(request, 'index.html', context)
