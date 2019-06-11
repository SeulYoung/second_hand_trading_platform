from django.shortcuts import render
from .models import Commodity
from account_app.models import Seller
from django.shortcuts import redirect, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json


def details(request):
    if request.method == "POST":
        commodity_id = request.POST.get("commodity_id")
        commodity = Commodity.objects.filter(commodity_id=commodity_id).first()
        similar_commodities = Commodity.objects.filter(type_id=commodity.type_id).first(3)
        return render(request, "details.html", {"commodity": commodity, "similar_commodities": similar_commodities})


@csrf_exempt
def upload_commodity(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode())
        for key in req.get('commodity_info'):
            seller = Seller.objects.filter(seller_id=request.user).first()
            Commodity.objects.create(seller_id=seller, type=key['type'], price=key['price'],
                                     pic=key['pic'], number=key['num'], name=key['commodity_name'],
                                     desc=key['desc'])

        return HttpResponse(json.dumps(req))
