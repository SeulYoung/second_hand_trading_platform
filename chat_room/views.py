from django.shortcuts import render, redirect
from account_app.models import Buyer, Seller
from chat_room.models import Communication
from django.http import JsonResponse


# Create your views here.
def chat_room(request):
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    if request.method == 'POST':
        seller_name = request.POST.get('seller_name')
        name_sort = [request.POST.get('seller_name'), str(request.user)]
        name_sort.sort()
        websocket_id = str(request.user) + '_' + request.POST.get('seller_name')
        print(seller_name+'******************'+websocket_id)
        return render(request, 'chat_app/chat_room.html',
                      {'websocket_id': websocket_id, 'room_name': seller_name, 'is_buyer': is_buyer,
                       'is_seller': is_seller})
    else:
        return redirect('index')


def get_new_message_list(request):
    if request.is_ajax():
        message = Communication.objects.values().filter(to_user=request.user.username)
        message_list = []
        if message.exists():
            message_list = list(message)
            print(message_list)

        return JsonResponse({"message_list": message_list}, safe=False)
