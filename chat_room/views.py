from django.shortcuts import render, redirect
from account_app.models import Buyer, Seller
from chat_room.models import Communication
from django.http import JsonResponse


# Create your views here.
def chat_room(request):
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    if request.method == 'POST':
        the_type = request.POST.get('type')
        if the_type == 'chat_seller':
            to_user = request.POST.get('seller_name')
            name_sort = [to_user, str(request.user)]
            name_sort.sort()
            websocket_id = str(request.user) + '_' + to_user
        elif the_type == 'chat_reply':
            to_user = request.POST.get('to_user')
            websocket_id = request.POST.get('webId')
        else:
            return redirect('index')
        return render(request, 'chat_app/chat_room.html',
                      {'websocket_id': websocket_id, 'room_name': to_user, 'is_buyer': is_buyer,
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
