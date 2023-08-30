from django.contrib import admin
from .models import AccountType, Account
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    list_display = ['user', 'account_type']


admin.site.register(AccountType)
