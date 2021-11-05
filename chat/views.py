from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse


# Create your views here.
def homeView(request):
    return render(request, 'home.html')
    
def roomView(request, room):
    username = request.GET['username']
    room_details = Room.objects.get(name=room)
    context = {
        'username': username,
        'room': room,
        'room_details': room_details
    }
    return render(request, 'room.html', context)

def checkView(request):        
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():   #validamos si el nombre del room existe
        return redirect('/'+room+'/?username='+username) #si existe lo redireccionamos a la sala con ese nombre
    else:
        new_room= Room.objects.create(name=room)  #creamos una sala con el nuevo nombre
        new_room.save()
        return redirect('/'+room+'/?username='+username)  

def sendView(request):
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']

    new_message = Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message sent succesfully')
  
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})  #esto es en formato json para actualizar constantemente en el lado del cliente