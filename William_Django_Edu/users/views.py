from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# 这里添加你继承的Form
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # for elem in form.fields:
        #     print('field name :', elem)
        #     print('field label:', form.fields[elem].label)
        #     print('field text:', form.fields[elem].help_text)
        #     print('-----------------------------')
        form.fields['username'].label = '用户名'
        form.fields['username'].help_text = '在此输入用户名'

        form.fields['email'].label = '邮箱'
        form.fields['email'].help_text = '在此输入邮箱'

        form.fields['password1'].label = '密码'
        form.fields['password1'].help_text = '在此输入密码'

        form.fields['password2'].label = '再次输入密码'
        form.fields['password2'].help_text = '再次输入密码'

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'【{username}】账号成功创建~您可以输入您的账号与密码登陆')
            return redirect('login')
    else:
        form = UserRegisterForm()
        form.fields['username'].label = '用户名'
        form.fields['username'].help_text = '在此输入用户名'

        form.fields['email'].label = '邮箱'
        form.fields['email'].help_text = '在此输入邮箱'

        form.fields['password1'].label = '密码'
        form.fields['password1'].help_text = '在此输入密码'

        form.fields['password2'].label = '再次输入密码'
        form.fields['password2'].help_text = '再次输入密码'

    return render(request, 'users/register.html', {'form': form})
