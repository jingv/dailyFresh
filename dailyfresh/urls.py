"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from df_goods import views as df_goods_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 用户中心页
    url(r'^user/', include('df_user.urls')),
    # tinymce配置
    url(r'tinymce/', include('tinymce.urls')),
    # 商品相关页以及主页
    url(r'^$', df_goods_views.index),
    url(r'^goods/', include('df_goods.urls')),
    # 购物车页面
    url(r'^cart/', include('df_cart.urls')),
]
