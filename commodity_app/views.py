from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from account_app.models import Seller, Buyer
from .models import Commodity, Order, Comment


def details(request):
    if request.method == "POST":
        commodity_id = request.POST.get("commodity_id")
        commodity = Commodity.objects.filter(commodity_id=commodity_id).first()

        orders = Order.objects.filter(commodity_id=commodity_id)
        comments = []
        for order in orders:
            buyer = Buyer.objects.filter(buyer_id=order.buyer_id).first()
            comment = Comment.objects.filter(order_id=order.order_id).first()
            comments.append(buyer.nickName + ":\n" + comment.content)
        similar_commodities = Commodity.objects.filter(type=commodity.type)
        return render(request, "details.html", {"commodity": commodity,
                                                "comments": comments,
                                                "similar_commodities": similar_commodities})


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
    # if request.method == "POST":
    return render(request, 'favorites.html')
