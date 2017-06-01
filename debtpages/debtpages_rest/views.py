from django.contrib.auth.models import User
from rest_framework import generics
from debtpages_rest.serializers import *
from debtpages_rest.models import Debt
from rest_framework import permissions
from debtpages_rest.permissions import *

class DebtList(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = (permissions.IsAuthenticated,
	    DebtListPermissions,)

    def perform_create(self, serializer):
        serializer.save(borrower=self.request.user)

class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtDetailSerializer
    permission_classes = (permissions.IsAuthenticated,
	    DebtPermissions,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,
AdminPermissions,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,
UserPermissions,)

class UserSumList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSumSerializer
    permission_classes = (permissions.IsAuthenticated,
AdminPermissions,)

class UserSumDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSumSerializer
    permission_classes = (permissions.IsAuthenticated,
UserPermissions,)
