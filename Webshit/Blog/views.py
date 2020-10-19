from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def Homepage(request):
    context = {
        'title': 'Homepage',
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
