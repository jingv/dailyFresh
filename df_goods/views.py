from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def index(request):
    # 每一个商品类别挑选四个当前时令的商品和四个点击率最高的商品
    # 以0结尾的为当前时令的商品， 已1结尾的为点击率较高的商品
    typelist = models.TypeInfo.objects.all()

    type00 = typelist[0].goodsinfo_set.order_by('-pk')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-goods_click')[0:4]
    type10 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-goods_click')[0:4]
    type20 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-goods_click')[0:4]
    type30 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-goods_click')[0:4]
    type40 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-goods_click')[0:4]
    type50 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-goods_click')[0:4]

    context = {
        'title': '天天生鲜-首页',
        'type0': typelist[0].id,
        'type00': type00,
        'type01': type01,
        'type1': typelist[1].id,
        'type10': type10,
        'type11': type11,
        'type2': typelist[2].id,
        'type20': type20,
        'type21': type21,
        'type3': typelist[3].id,
        'type30': type30,
        'type31': type31,
        'type4': typelist[4].id,
        'type40': type40,
        'type41': type41,
        'type5': typelist[5].id,
        'type50': type50,
        'type51': type51,
    }

    return render(request, 'df_goods/index.html', context)


def list(request, type_id, page_index, sort_rules):
    typelist = models.TypeInfo.objects.all()

    typeinfo = models.TypeInfo.objects.get(pk=type_id)
    news = typeinfo.goodsinfo_set.order_by('id')[0:2]
    # sort_rules 默认为1：按照最新排序， 值为2：按照价格， 值为3：按照人气排序
    if sort_rules == '1':
        goods_list = models.GoodsInfo.objects.filter(goods_type_id=type_id).order_by('-id')
    elif sort_rules == '2':
        goods_list = models.GoodsInfo.objects.filter(goods_type_id=type_id).order_by('-goods_price')
    else:
        goods_list = models.GoodsInfo.objects.filter(goods_type_id=type_id).order_by('-goods_click')

    # 对获得的数据进行分页操作， 获取相应页面的数据
    paginator = Paginator(goods_list, 10)
    page_lsit = paginator.page(int(page_index))

    context = {
        'title': '天天生鲜' + typeinfo.type_title,
        'page_list': page_lsit,
        'paginator': paginator,
        'typeinfo': typeinfo,
        'sort_rules': sort_rules,
        'news': news,
        'type0': typelist[0].id,
        'type1': typelist[1].id,
        'type2': typelist[2].id,
        'type3': typelist[3].id,
        'type4': typelist[4].id,
        'type5': typelist[5].id,
    }

    return render(request, 'df_goods/list.html', context)


def detail(request, goods_id):
    typelist = models.TypeInfo.objects.all()

    goods = models.GoodsInfo.objects.get(pk=int(goods_id))
    goods.goods_click += 1
    goods.save()
    news = goods.goods_type.goodsinfo_set.order_by('-id')[0:2]
    goods_describe = str(goods.goods_detail)[3: -4]
    context = {
        'title': '天天生鲜' + goods.goods_type.type_title,
        'goods': goods,
        'goods_describe': goods_describe,
        'news': news,
        'goods_id': goods_id,
        'type0': typelist[0].id,
        'type1': typelist[1].id,
        'type2': typelist[2].id,
        'type3': typelist[3].id,
        'type4': typelist[4].id,
        'type5': typelist[5].id,
    }
    return render(request, 'df_goods/detail.html', context)
