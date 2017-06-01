from back.models import *
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from back.serializers import *
from back.permissions import *
from django.contrib.auth.models import User
import json

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated,
            RoomListPermissions,)

class RoomDetail(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permissions_classes = (permissions.IsAuthenticated,
            DefaultPermissions,)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def HistoryList(request, pk):
    try:
        history = History.objects.filter(room__id = pk)
    except History.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    room = Room.objects.get(pk = pk)
    past = history.order_by('-id')[0].player if history.count() > 0 else room.player2;

    serializer = HistorySerializer(history, many = True)
    if request.method == 'GET':
        return Response(serializer.data) 
    elif request.method == 'POST':
        if (request.user == room.player1 or request.user == room.player2) and request.user != past:
            hist = History()
            hist.place_i = request.data['place_i']
            hist.place_j = request.data['place_j']
            hist.player = request.user
            hist.room = room
            hist.save()
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)

        return Response(status = status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def room_players_list(request, pk):
    try:
        room = Room.objects.get(pk = pk)
    except Room.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = PlayerSerializer(room)
    if request.method == 'GET':
        return Response(serializer.data)
    elif request.method == 'POST':
        if room.player1 == None:
            room.player1 = request.user
            room.save()
        elif room.player2 == None:
            room.player2 = request.user
            room.save()
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
        return Response(status = status.HTTP_201_CREATED)
