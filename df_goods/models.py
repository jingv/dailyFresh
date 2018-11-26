from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    type_title = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        # py3 中不需要进行转码
        return self.type_title
        # py2 中需要进行转码
        # return self.type_title.encode('utf-8')


class GoodsInfo(models.Model):
    """创建商品类模型"""
    goods_title = models.CharField(max_length=10)
    goods_pic = models.ImageField(upload_to='df_goods')
    goods_price = models.DecimalField(max_digits=5, decimal_places=2)
    # 商品单位
    goods_price_unit = models.CharField(max_length=10, default='500g')
    isDelete = models.BooleanField(default=False)
    # 商品热度
    goods_click = models.IntegerField(default=0)
    # 商品简介
    goods_describe = models.CharField(max_length=100)
    # 商品库存
    goods_left = models.IntegerField(default=0)
    # 商品详情
    goods_detail = HTMLField()
    goods_detail_pic = models.ImageField(upload_to='df_goods', null=True)
    goods_type = models.ForeignKey(TypeInfo, on_delete=models.DO_NOTHING)
    # 是否在首页推荐
    # goods_adv = models.BooleanField(default=False)

    def __str__(self):
        return self.goods_title
