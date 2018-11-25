from hashlib import sha1
from django.shortcuts import render, redirect
from . import models


def register(request):
    context = {
        'title': '天天生鲜-注册'
    }
    return render(request, 'df_user/register.html', context)


def register_handle(request):
    # 接受用户信息
    post = request.POST
    user_name = post.get('user_name')
    user_pwd = post.get('pwd')
    user_cpwd = post.get('cpwd')
    user_email = post.get('email')

    if user_cpwd != user_pwd:
        return redirect('/user/register/')

    # 密码加密
    s = sha1()
    s.update(user_pwd.encode(encoding='utf-8'))
    user_pwd_sha1 = s.hexdigest()

    user = models.UserInfo()
    user.user_name = user_name
    user.user_pwd = user_pwd_sha1
    user.user_email = user_email

    user.save()

    # 注册成功， 转到登陆页面
    return redirect('/user/login/')
