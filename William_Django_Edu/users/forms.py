from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # 这里可以自定义label以及help_text(说明文字)
        # labels = {
        #     'username': '用户名称'
        # }
        # help_texts = {
        #     'username': '这里写入用户名称'
        # }
