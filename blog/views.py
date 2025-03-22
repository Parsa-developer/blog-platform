from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, SignUpForm
from django.contrib.auth.views import LoginView, LogoutView

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    success_url = reverse_lazy('post_list')

class CustomLogoutView(LogoutView):
    next_page = 'post_list'

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'blog/signup.html'
    success_url = reverse_lazy('login')