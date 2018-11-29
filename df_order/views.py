from datetime import datetime
from django.shortcuts import render, redirect
from django.db import transaction
from df_user.models import UserInfo
from df_cart.models import CartInfo
from df_user import user_decorator
from . import models


# 初始化订单页面
@user_decorator.login
def order(request):
    # 获取用户
    user = UserInfo.objects.get(id=request.session['user_id'])
    # 根据get提交的数据查询购物车的信息
    get = request.GET
    cart_id_list = [int(i) for i in get.getlist('cart_id')]
    # 查询购物车表中数据, 一个id对应一条购物车实录
    cart_goods_list = CartInfo.objects.filter(id__in=cart_id_list)
    # 构造传递的数据
    context = {
        'title': '提交订单',
        'cart_goods_list': cart_goods_list,
        'user': user,
        # 商品编号 5, 6， 在用户将商品添加到订单后，将数据转发给order_handler
        'cart_ids': get.getlist('cart_id'),
    }
    return render(request, 'df_order/order.html', context)


@transaction.atomic()
@user_decorator.login
def order_handler(request):
    # 一旦操作失败全部回退
    #     1、创建订单对象
    #     2、判断商品的库存
    #     3、创建详单对象
    #     4、修改商品库存
    #     5、删除购物车商品

    # 创建事务回退的点
    tran_id = transaction.savepoint()
    # 接收购物车编号
    cart_ids = request.GET.get('cart_ids')

    try:
        # 创建订单对象
        order = models.OrderInfo()
        user_id = request.session['user_id']
        now = datetime.now()
        now_str = now.strftime('%x').replace('/', '') + now.strftime('%X')
        order.order_id = '%s%d' % (now_str, user_id)
        order.user = UserInfo.objects.get(id=user_id)
        order.order_date = now_str
        order.order_total_price = eval(request.GET.get('total_price'))
        order.save()
        # 创建详单对象
        cart_ids = [int(i) for i in eval(cart_ids)]
        for cart_id in cart_ids:
            detail = models.OrderDetailInfo()
            detail.order = order
            # 查询购物车信息
            cart = CartInfo.objects.get(id=cart_id)
            # print('==========================', cart_id)
            # 判断商品库存
            goods = cart.goods
            if goods.goods_left >= cart.count:
                goods.goods_left -= cart.count
                goods.save()
                # 完善详单信息
                detail.goods_id = goods.id
                detail.price = goods.goods_price
                detail.count = cart.count
                detail.save()
                # 删除购物车数据
                # print('==================', 'delete')
                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
    except Exception as e:
        transaction.savepoint_rollback(tran_id)
        return redirect('/cart/')

    return redirect('/user/user_order_1/')


@user_decorator.login
def pay(request, order_id):
    order = models.OrderInfo.objects.get(order_id=order_id)
    order.isPay = True
    order.save()
    context = {
        'order': order,
    }
    return render(request, 'df_order/pay.html', context)
