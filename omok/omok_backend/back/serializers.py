from rest_framework import serializers
from back.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class RoomSerializer(serializers.ModelSerializer):
    player1 = serializers.ReadOnlyField(source='player1.id')
    player2 = serializers.ReadOnlyField(source='player2.id')
    turn = serializers.SerializerMethodField()
    win = serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = ('id', 'player1', 'player2', 'turn', 'win')

    def get_turn(self, obj):
        return History.objects.filter(room=obj.id).count() + 1

    def get_win(self, obj):
        m = [[0 for x in range(19)] for y in range(19)]
        for e in History.objects.filter(room=obj.id):
            if e.player.id == obj.player1.id:
                m[e.place_i][e.place_j] = 1
                val = 1
            else:
                m[e.place_i][e.place_j] = 2
                val = 2

            count = 1
            i = e.place_i
            j = e.place_j
            k = 1

            while count < 5 and j+k < 19 and m[i][j+k] == val:
                k+=1
                count+=1
            k = 1
            while count < 5 and j-k >= 0 and m[i][j-k] == val:
                k+=1
                count+=1

            if count == 5:
                return val

            count = 1
            k = 1

            while count < 5 and i+k < 19 and m[i+k][j] == val:
                k+=1
                count+=1
            k = 1
            while count < 5 and i-k >= 0 and m[i-k][j] == val:
                k+=1
                count+=1

            if count == 5:
                return val

            count = 1
            k = 1

            while count < 5 and i+k < 19 and j+k < 19 and m[i+k][j+k] == val:
                k+=1
                count+=1
            k = 1
            while count < 5 and i-k >= 0 and j-k >= 0 and m[i-k][j-k] == val:
                k+=1
                count+=1

            if count == 5:
                return val

            count = 1
            k = 1

            while count < 5 and i+k < 19 and j-k >= 0 and m[i+k][j-k] == val:
                k+=1
                count+=1
            k = 1
            while count < 5 and i-k >= 0 and j+k < 19 and m[i-k][j+k] == val:
                k+=1
                count+=1

            if count == 5:
                return val

        return 0

class PlayerSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        l1 = ([ obj.player1.id ] if obj.player1 else [])
        l2 = ([ obj.player2.id ] if obj.player2 else [])
        return l1 + l2

    class Meta:
        model = Room

class HistorySerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'player': obj.player.id,
            'room': obj.room.id,
            'place_i': obj.place_i,
            'place_j': obj.place_j
        }

