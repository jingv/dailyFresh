from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.index),
    # 三个数字分别为商品的类别、第几页、以及排序方式
    url(r'^list(\d)_(\d)_(\d)/$', views.list),
    url(r'^(\d)+/$', views.detail),
]
