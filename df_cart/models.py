from django.db import models

from df_goods.models import GoodsInfo
from df_user.models import UserInfo


class CartInfo(models.Model):
    # 引用外部模块的方法
    # user = models.ForeignKey('df_user.UserInfo')
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    goods = models.ForeignKey(GoodsInfo, on_delete=models.DO_NOTHING)
    # 购买商品的数量
    count = models.IntegerField()
