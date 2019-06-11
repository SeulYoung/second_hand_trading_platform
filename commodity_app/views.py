import json

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account_app.models import Seller
from .models import Commodity


def details(request):
    if request.method == "POST":
        commodity_id = request.POST.get("commodity_id")
        commodity = Commodity.objects.filter(commodity_id=commodity_id).first()
        similar_commodities = Commodity.objects.filter(type=commodity.type)
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
