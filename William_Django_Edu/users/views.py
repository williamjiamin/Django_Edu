from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# 这里添加你继承的Form
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        u_form.fields['username'].label = '用户名'
        u_form.fields['username'].help_text = '在此输入用户名'

        u_form.fields['email'].label = '邮箱'
        u_form.fields['email'].help_text = '在此输入邮箱'

        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)

        p_form.fields['image'].label = '头像'
        p_form.fields['image'].help_text = '在此上传头像'

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'您的账号信息已经被成功更新！')

            # Post/Redirect/Get


            # 假设用户提交了一个表单（submit--->POST---->server----->2XX success---->refresh---->POST）
            # PRG(submit---->POST---->server--->3XX Redirect---->Get---->2XX success---->refresh)

            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        u_form.fields['username'].label = '用户名'
        u_form.fields['username'].help_text = '在此输入用户名'

        u_form.fields['email'].label = '邮箱'
        u_form.fields['email'].help_text = '在此输入邮箱'

        p_form = ProfileUpdateForm(instance=request.user.profile)

        p_form.fields['image'].label = '头像'
        p_form.fields['image'].help_text = '在此上传头像'

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
