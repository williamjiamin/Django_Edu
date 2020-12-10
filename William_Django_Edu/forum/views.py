from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'forum/about.html', {'title': '关于页面'})
