from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>大家好，这个页面是乐学偶得Django的主页</h1>')
