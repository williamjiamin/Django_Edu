from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin


# posts = [
#     {
#         'author': 'William',
#         'title': '这个是William发的帖子标题',
#         'content': '这是这个帖子的内容',
#         'date_posted': '2021,1,1'
#     },
#     {
#         'author': 'Mary',
#         'title': '这个是Mary发的帖子标题',
#         'content': '这是这个帖子的内容',
#         'date_posted': '2022,2,2'
#     }
# ]


# def home(request):
#     return HttpResponse('<h1>大家好，这个页面是乐学偶得论坛的主页</h1>')
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': '主页'
    }
    return render(request, 'forum/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'forum/home.html'  # <app_name>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'forum/about.html', {'title': '关于页面'})
