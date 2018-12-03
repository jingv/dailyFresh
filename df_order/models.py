from django.db import models

from df_goods.models import GoodsInfo
from df_user.models import UserInfo


class OrderInfo(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now=True)
    isPay = models.BooleanField(default=False)
    order_total_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_address = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(OrderInfo, on_delete=models.DO_NOTHING)
    # 商品单价
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField()
