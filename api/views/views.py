from django.shortcuts import get_object_or_404, redirect, render
from ..models import Post, Category, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.base import View
from ..forms import CommentForm, AddCategoryForm, AddPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().select_related('owner')
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post_id = context['post'].id
        context['comments'] = Comment.objects.filter(post_id=post_id).select_related('post').select_related('owner')
        context["form"] = CommentForm()
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'api/addpost.html'
    login_url = 'login'

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super(AddPostView, self).form_valid(form)


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category_id = context['category'].id
        context['posts'] = Post.objects.filter(categories=category_id).prefetch_related('categories').select_related('owner')
        return context


class AddCategoryView(LoginRequiredMixin, CreateView):
    form_class = AddCategoryForm
    template_name = 'api/addcategory.html'
    login_url = 'login'


class AddCommentView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.owner = request.user
            form.save()
            return redirect(post.get_absolute_url())


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    
    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class EditProfileView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = User 
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = "registration/user_form.html"

    def get_success_url(self):
        return reverse('home')


class UserProifleDetailView(DetailView):
    model = User
    template_name = "registration/user_detail.html"