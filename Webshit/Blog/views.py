from django.shortcuts import render
from .models import Post

# Create your views here.
def Homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
