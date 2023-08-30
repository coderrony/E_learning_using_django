from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AccountType(models.Model):
    account_type = models.CharField(max_length=264)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.account_type)


class Account(models.Model):
    account_type = models.ForeignKey(
        AccountType, on_delete=models.CASCADE, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="account_user", unique=True)

    def __str__(self) -> str:
        return str(self.user)
