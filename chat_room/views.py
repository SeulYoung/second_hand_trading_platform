from django.shortcuts import render
from account_app.models import Buyer, Seller
from chat_room.models import Communication
from django.http import JsonResponse


# Create your views here.
def chat_room(request):
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    return render(request, 'chat_app/chat_room.html', {'room_name': '小阳商城', 'is_buyer': is_buyer,
                                                       'is_seller': is_seller})


def get_new_message_list(request):
    if request.is_ajax():
        message = Communication.objects.values().filter(to_user=request.user.username)
        message_list = []
        if message.exists():
            message_list = list(message)
            print(message_list)

        return JsonResponse({"message_list": message_list}, safe=False)
