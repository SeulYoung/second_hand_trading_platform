from django.shortcuts import render
from .models import Commodity


def details(request):
    if request.method == "POST":
        commodity_id = request.POST.get("commodity_id")
        commodity = Commodity.objects.filter(commodity_id=commodity_id).first()
        return render(request, "details.html", {"commodity": commodity})
