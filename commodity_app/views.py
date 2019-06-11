from django.shortcuts import render
from .models import Commodity
import json


def details(request):
    if request.method == "POST":
        commodity_id = request.POST.get("commodity_id")
        commodity = Commodity.objects.filter(commodity_id=commodity_id).first()
        similar_commodities = Commodity.objects.filter(type_id=commodity.type_id).first(3)
        return render(request, "details.html", {"commodity": commodity, "similar_commodities": similar_commodities})


def upload_commodity(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode())

