from django.db import models
from django.contrib.auth.models import User

class Debt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default = 0)
    borrower = models.ForeignKey(User, related_name='debts_as_borrower', on_delete=models.CASCADE)
    lender = models.ForeignKey(User, related_name='debts_as_lender', on_delete=models.CASCADE)
