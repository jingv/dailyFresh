from django.contrib import admin
from . import models


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'type_title', 'isDelete']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['pk', 'goods_title', 'goods_pic', 'goods_detail_pic', 'goods_price', 'goods_price_unit', 'isDelete', 'goods_click', 'goods_describe','goods_left', 'goods_detail', 'goods_type']


admin.site.register(models.TypeInfo, TypeInfoAdmin)
admin.site.register(models.GoodsInfo, GoodsInfoAdmin)
