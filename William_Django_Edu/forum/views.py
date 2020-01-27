from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'William',
        'title': '这个是William发的帖子标题',
        'content': '这是这个帖子的内容',
        'date_posted': '2021,1,1'
    },
    {
        'author': 'Mary',
        'title': '这个是Mary发的帖子标题',
        'content': '这是这个帖子的内容',
        'date_posted': '2022,2,2'
    },
]


# def home(request):
#     return HttpResponse('<h1>大家好，这个页面是乐学偶得论坛的主页</h1>')
def home(request):
    return render(request, 'forum/home.html')


def about(request):
    return HttpResponse('<h1>大家好，这个页面是乐学偶得论坛的关于页面</h1>')
