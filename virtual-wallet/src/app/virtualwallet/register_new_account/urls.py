"""Url register New Account API module"""

from django.urls import path, include
from register_new_account.views import RegisterNewAccountController

urlpatterns = [
    path('', RegisterNewAccountController.as_view())
]