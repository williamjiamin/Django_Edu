from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
        # 这里可以自定义label以及help_text(说明文字)
        # labels = {
        #     'username': '用户名称',
        # }
        # help_texts = {
        #     'username': '这里写入用户名称',
        # }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', ]

        # labels = {
        #     'username': '用户名称',
        #     'email': '邮箱',
        #
        # }
        # help_texts = {
        #     'username': '这里写入用户名称',
        #     'email': '这里输入邮箱账号',
        # }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', ]

        # labels = {
        #     'image': '用户头像',
        #
        # }
        # help_texts = {
        #     'image': '这里上传用户头像',
        # }
