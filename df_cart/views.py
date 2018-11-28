from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import models
from df_user import user_decorator


@user_decorator.login
def cart(request):
    user_id = request.session['user_id']
    cart_goods = models.CartInfo.objects.filter(user_id=user_id)
    context = {
        'title': '购物车',
        'page_num': 1,
        'cart_goods': cart_goods,
        'goods_count': cart_goods.count(),
    }
    return render(request, 'df_cart/cart.html', context)


@user_decorator.login
# 返回购物车商品种类的数量
def cart_goods_type_count(request):
    user_id = request.session['user_id']
    cart_goods = models.CartInfo.objects.filter(user_id=user_id)
    data = {
        'goods_count': cart_goods.count(),
    }
    return JsonResponse(data)


@user_decorator.login
def add(request, goods_id, goods_count):
    user_id = request.session['user_id']
    goods_id = int(goods_id)
    goods_count = int(goods_count)

    # 查询用户是否已经将当前商品加入到购物车，如果已经加入到购物车，就将原有的购物车对应商品数量+1， 如果没有则将当前商品加入到购物车
    cart_goods = models.CartInfo.objects.filter(user_id=user_id, goods_id=goods_id)
    if len(cart_goods) >= 1:
        cart = cart_goods[0]
        cart.count += goods_count
    else:
        cart = models.CartInfo()
        cart.user_id = user_id
        cart.goods_id = goods_id
        cart.count = goods_count
    cart.save()

    # 判断当前请求是不是ajax请求方式，如果是则返回已购买商品的数量（是ajax说明是在商品详情页购买的商品，在该页面购买商品无需跳转到购物车，直接在右上角显示购买商品种类的数量即可），如果不是则将页面重定向至购物车页面
    if request.is_ajax():
        # 商品种类的数量
        count = models.CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'goods_count': count})
    else:
        return redirect('/cart/')


@user_decorator.login
def edit(request, cart_id, count):
    cart = models.CartInfo.objects.get(pk=int(cart_id))
    # count1 为原先货物的数量的值
    count1 = cart.count
    try:
        cart.count = int(count)
        cart.save()
        data = {
            'ok': 0,
        }
    except Exception as e:
        data = {
            'ok': count1,
        }
    return JsonResponse(data)


@user_decorator.login
def delete(request, cart_id):
    try:
        cart = models.CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {
            'ok': 1,
        }
    except Exception as e:
        data = {
            'ok': 0,
        }
    return JsonResponse(data)
