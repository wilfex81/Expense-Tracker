from django.db import models



class Account(models.Model):
    LIST = [
        ('Account Options',(
                    ('M-Pesa', 'M-Pesa'),
                    ('Bank', 'Bank'),
                    ('Credit_Card', 'Credit_Card'),
                )
            
        ),
        
    ]

    TYPE_OF_INCOME = [
        ('Account Options',(
                    ('salary', 'salary'),
                    ('saving', 'saving'),
                    ('investment', 'investment'),
                )
        ), 
    ]
    account_name = models.CharField(max_length=50, choices=LIST)
    saving_list = models.CharField(max_length=50, choices=TYPE_OF_INCOME)
    deposited_amount = models.DecimalField(max_digits=15, decimal_places=2)
    deposited_date = models.DateField()


    def __str__(self)-> str:
        return f"{self.account_name}: {self.deposited_amount}"


class BudgetCategorie(models.Model):
    title = models.CharField(max_length=100, help_text='e.g. Utilities, groceries, etc.')
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    date_budgeted = models.DateField()

    def __str__(self)-> str:
        return f"{self.title}: {self.budget}"

class Transaction(models.Model):
    description = models.CharField(max_length=200, help_text='store name')
    trasaction_date = models.DateField()
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    budget_categorie = models.ForeignKey(BudgetCategorie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.description} : {self.trasaction_date}"
    
