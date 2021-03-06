from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from account_app.models import Seller, Buyer
from .models import Commodity, Order, Comment, Favorites


def details(request):
    if request.method == "POST":
        if "favorite" in request.POST:
            try:
                commodity_id = request.POST.get("commodity_id")
                buyer = Buyer.objects.filter(buyer_id=request.user).first()
                commodity = Commodity.objects.filter(commodity_id=commodity_id).first()

                favorite = Favorites.objects.filter(buyer_id=buyer, commodity_id=commodity)
                if not favorite:
                    Favorites.objects.create(buyer_id=buyer, commodity_id=commodity)
            except Exception as e:
                print(e)
        else:
            is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
            is_seller = Seller.objects.filter(seller_id=request.user).first()
            commodity_id = request.POST.get("commodity_id")
            commodity = Commodity.objects.filter(commodity_id=commodity_id).first()

            orders = Order.objects.filter(commodity_id=commodity_id)
            comments = []
            for order in orders:
                buyer = Buyer.objects.filter(buyer_id=order.buyer_id.buyer_id).first()
                comment = Comment.objects.filter(order_id=order).first()
                if comment:
                    comments.append(buyer.nickName + ":\n" + comment.content)
            similar_commodities = Commodity.objects.filter(type=commodity.type)
            return render(request, "details.html", {"commodity": commodity,
                                                    "comments": comments,
                                                    "similar_commodities": similar_commodities,
                                                    'is_buyer': is_buyer, 'is_seller': is_seller})


def buy(request):
    if request.method == "POST":
        commodity_id = request.POST.get("commodity_id")
        num = request.POST.get("num")

        is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
        is_seller = Seller.objects.filter(seller_id=request.user).first()
        commodity = Commodity.objects.filter(commodity_id=commodity_id).first()
        total_price = int(num) * commodity.price
        return render(request, "buy.html", {"commodity": commodity, "num": num, "total_price": total_price,
                                            'is_buyer': is_buyer, 'is_seller': is_seller})


def create_order(request):
    if request.method == "POST":
        commodity_id = request.POST.get("commodity_id")
        buyer = Buyer.objects.filter(buyer_id=request.user).first()
        commodity = Commodity.objects.filter(commodity_id=commodity_id).first()
        Order.objects.create(buyer_id=buyer, commodity_id=commodity, status="已付款")

        is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
        is_seller = Seller.objects.filter(seller_id=request.user).first()
        commodity = Commodity.objects.filter(commodity_id=commodity_id).first()
        orders = Order.objects.filter(commodity_id=commodity_id)
        comments = []
        for order in orders:
            buyer = Buyer.objects.filter(buyer_id=order.buyer_id.buyer_id).first()
            comment = Comment.objects.filter(order_id=order).first()
            if comment:
                comments.append(buyer.nickName + ":\n" + comment.content)
        similar_commodities = Commodity.objects.filter(type=commodity.type)
        return render(request, "details.html", {"commodity": commodity,
                                                "comments": comments,
                                                "similar_commodities": similar_commodities,
                                                'is_buyer': is_buyer, 'is_seller': is_seller})


@csrf_exempt
def upload_commodity(request):
    if request.method == 'POST':
        seller = Seller.objects.filter(seller_id=request.user).first()
        type = request.POST.get('type')
        price = request.POST.get('price')
        pic = request.FILES.get('pic')
        number = request.POST.get('num')
        name = request.POST.get('commodity_name')
        desc = request.POST.get('desc')
        Commodity.objects.create(seller_id=seller, type=type, pic=pic, number=number, price=price,
                                 name=name, desc=desc)
        return redirect('sellerhome')


def favorites(request):
    seller = Seller.objects.filter(seller_id=request.user).first()
    buyer = Buyer.objects.filter(buyer_id=request.user).first()
    com_id = Favorites.objects.filter(buyer_id=buyer)
    if com_id:
        is_exit = True
    else:
        is_exit = False

    return render(request, 'favorites.html',
                  {'fav_commodity': com_id, 'judge': is_exit, 'is_buyer': buyer, 'is_seller': seller})


def order(request):
    seller = Seller.objects.filter(seller_id=request.user).first()
    buyer = Buyer.objects.filter(buyer_id=request.user).first()
    order_list = Order.objects.filter(buyer_id=buyer)
    if order_list:
        judge = True
    else:
        judge = False
    return render(request, 'order.html',
                  {'order_list': order_list, 'judge': judge, 'is_buyer': buyer, 'is_seller': seller})


def order_info(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order_content = Order.objects.filter(order_id=order_id).first()
        is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
        is_seller = Seller.objects.filter(seller_id=request.user).first()

        return render(request, 'order_content.html', {'content': order_content, 'is_buyer': is_buyer,
                                                      'is_seller': is_seller})


def deal_confirm(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        Order.objects.filter(order_id=order_id).update(status='已收货')
        order_content = Order.objects.filter(order_id=order_id).first()
        is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
        is_seller = Seller.objects.filter(seller_id=request.user).first()

        return render(request, 'order_content.html', {'content': order_content, 'is_buyer': is_buyer,
                                                      'is_seller': is_seller})


def fall_commodity(request):
    if request.method == 'POST':
        commodity_id = request.POST.get('commodity_id')
        Commodity.objects.filter(commodity_id=commodity_id).delete()

        return redirect('sellerhome')


def clear_favor(request):
    buyer = Buyer.objects.filter(buyer_id=request.user).first()
    favors = Favorites.objects.filter(buyer_id=buyer).all().delete()

    return redirect('favorites')
