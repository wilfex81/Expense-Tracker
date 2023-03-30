from django.contrib import admin
from decimal import Decimal

from .models import Account, BudgetCategorie


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_name", "deposited_amount", "deposited_date")

    def total_budget_amount(self, total_amount):
        items = Account.objects.filter(deposited_amount=total_amount)
        self.total_amount = 0
        for item in items:
            total_amount += item.deposited_amount
        return total_amount

    total_budget_amount.short_description = "Total Budget"
@admin.register(BudgetCategorie)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("title", "budget", "date_budgeted")

    def save_model(self, request, obj, form, change):
        # Parse the budget field to extract the decimal number
        budget_str = form.cleaned_data['budget']
        print(f'budget_str = {budget_str}')
        try:
            budget = Decimal(budget_str)
        except ValueError:
            raise ValidationError('Budget must be a decimal number.')
        print(f'budget = {budget}')

        # Set the budget field to the parsed decimal number
        obj.budget = budget
        obj.save()


    def total_budget_amount(self, total_amount):
        items = BudgetCategorie.objects.filter(budget=total_amount)
        self.total_amount = 0
        for item in items:
            total_amount += item.budget
        return total_amount

    total_budget_amount.short_description = "Total Budget"