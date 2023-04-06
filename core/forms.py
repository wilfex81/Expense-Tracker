from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'account_type', 'starting_balance', 'deposited_date')
        widgets = {
            'deposited_date': forms.DateInput(attrs={'id': 'datepicker', 'placeholder': 'MM/DD/YYYY'}),
        }
