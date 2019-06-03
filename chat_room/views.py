from django.shortcuts import render


# Create your views here.
def tem(request):
    return render(request, 'chat_app/index.html')


def chat_room(request):
    return render(request, 'chat_app/chat_room.html', {'room_name': '小阳商城'})
