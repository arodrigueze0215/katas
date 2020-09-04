import uuid

#Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    customer_id = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_number = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.get_full_name()}'

    @property
    def customer_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Account(models.Model):
    _STATUS = (
        ('0', 'CLOSED'),
        ('1', 'OPEN'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    account_id = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=_STATUS,default='1')
    balance = models.PositiveIntegerField(default=0)
    opening_date = models.DateField(auto_now=False)

    def __str__(self):
        return f'{self.account_id} {self.customer} {self.status} {self.balance} {self.opening_date}'

class Credit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    ammount = models.PositiveIntegerField()
    transaction_date = models.DateField(auto_now=False)
    description = models.CharField(max_length=1500)

class Debit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    ammount = models.PositiveIntegerField()
    transaction_date = models.DateField(auto_now=False)
    description = models.CharField(max_length=1500)