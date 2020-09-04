#Django
from django.contrib import admin

# Models.
from model.models import Customer, Account

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """This is how the customer model on admin dashboard look like"""
    list_display = ('customer_id', 'customer_name', 'person_number', 'phone_number')



@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """This is how the Account model on admin dashboard look like"""
    list_display = ('account_id', 'customer', 'status', 'balance', 'opening_date')
