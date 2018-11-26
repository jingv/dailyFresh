from django.http import HttpResponseRedirect


# 如果未登录则强制转换到登陆页面
def login(func):
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('user_name'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun
