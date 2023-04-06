from django.contrib import admin
from decimal import Decimal

from .models import Account, BudgetCategorie, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name","account_type", "starting_balance", "deposited_date")
@admin.register(BudgetCategorie)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "budget_amount", "budget_date")

    def total_budget_amount(self, total_amount):
        items = BudgetCategorie.objects.filter(budget=total_amount)
        self.total_amount = 0
        for item in items:
            total_amount += item.budget
        return total_amount

    total_budget_amount.short_description = "Total Budget"

@admin.register(Transaction)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("description", "trasaction_date")
