from django.contrib.auth.models import User
from rest_framework import generics
from debtpages_rest.serializers import UserSerializer, DebtSerializer, UserSumSerializer
from debtpages_rest.models import Debt
import debtpages_rest.permissions

class DebtList(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    def perform_create(self, serializer):
        serializer.save(borrower=self.request.user)

class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSumList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSumSerializer

class UserSumDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSumSerializer
