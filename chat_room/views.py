from django.shortcuts import render


# Create your views here.
def chat_room(request):
    return render(request, 'chat_app/chat_room.html')
