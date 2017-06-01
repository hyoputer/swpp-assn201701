from django.contrib.auth.models import User
from rest_framework import serializers
from debtpages_rest.models import Debt
from django.db.models import Sum

class UserSerializer(serializers.ModelSerializer):
    debts_as_borrower = serializers.PrimaryKeyRelatedField(many=True, queryset=Debt.objects.all())
    debts_as_lender = serializers.PrimaryKeyRelatedField(many=True, queryset=Debt.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'debts_as_borrower', 'debts_as_lender')

class DebtSerializer(serializers.ModelSerializer):
    borrower = serializers.ReadOnlyField(source='borrower.id') 
    class Meta:
        model = Debt
        fields = ('id', 'created', 'amount', 'borrower', 'lender')

class DebtDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id', 'created', 'amount', 'borrower', 'lender')

class UserSumSerializer(serializers.ModelSerializer):
    lended_money = serializers.SerializerMethodField()
    borrowed_money = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username', 'lended_money', 'borrowed_money')
     
    def get_lended_money(self, obj):
        a = Debt.objects.filter(lender__id = obj.id).aggregate(Sum('amount'))['amount__sum']
        if a is None:
     	    return 0
        else:
     	    return a

    def get_borrowed_money(self, obj):
        a = Debt.objects.filter(borrower__id = obj.id). aggregate(Sum('amount'))['amount__sum']
        if a is None:
            return 0
        else:
            return a
