from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^add(\d+)_(\d+)/$', views.add),
    url(r'^edit(\d+)_(\d+)/$', views.edit),
    url(r'^delete(\d+)/$', views.delete),
    # 返回购物车商品种类的数量
    url(r'^cart_goods_type_count/$', views.cart_goods_type_count),
]
