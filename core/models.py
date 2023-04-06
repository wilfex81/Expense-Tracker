from django.db import models



class Account(models.Model):
    name = models.CharField(max_length=255)
    ACCOUNT_TYPES = (
        ('Checking', 'Checking'),
        ('Savings', 'Savings'),
        ('Credit Card', 'Credit Card'),
        ('Cash', 'Cash'),
        ('Investment', 'Investment'),
        ('M-Pesa', 'M-Pesa'),
    )
    account_type = models.CharField(max_length=255, choices=ACCOUNT_TYPES)
    starting_balance = models.DecimalField(max_digits=10, decimal_places=2)
    deposited_date = models.DateField()


    def __str__(self)-> str:
        return f"{self.name}: {self.account_type}"


class BudgetCategorie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    budget_date = models.DateTimeField()

    def __str__(self)-> str:
        return f"{self.name}: {self.budget_amount}"

class Transaction(models.Model):
    description = models.CharField(max_length=200, help_text='store name')
    trasaction_date = models.DateField()
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    budget_categorie = models.ForeignKey(BudgetCategorie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.description} : {self.trasaction_date}"
    
