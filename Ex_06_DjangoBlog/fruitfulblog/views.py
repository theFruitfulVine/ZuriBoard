from django.shortcuts import render
from .models import Post

# Create your views here.
def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'fruitfulblog/home.html', context)

def about(request):
    return render(request, 'fruitfulblog/about.html', {'title': 'About'})