from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.
def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'fruitfulblog/home.html', context)

class PostListView(ListView): #class-based view
    model = Post
    template_name = 'fruitfulblog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView): #class-based view
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #class-based view
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #allow post updates
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #prevent updating/editing another user's post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #delete posts
    model = Post
    success_url = '/'
    
    def test_func(self): #prevent updating/editing another user's post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'fruitfulblog/about.html', {'title': 'About'})