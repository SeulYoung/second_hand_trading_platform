from django.shortcuts import render
from account_app.models import Buyer, Seller


# Create your views here.
def chat_room(request):
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    return render(request, 'chat_app/chat_room.html', {'room_name': '小阳商城', 'is_buyer': is_buyer,
                                                       'is_seller': is_seller})
