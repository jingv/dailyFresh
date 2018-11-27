from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    # url(r'^$',  views.index),
    # 商品列表页：三个数字分别为商品的类别、第几页、以及排序方式
    url(r'^list(\d)_(\d)_(\d)/$', views.list),
    # 商品详情页
    url(r'^(\d)+/$', views.detail),
]
