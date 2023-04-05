from django.shortcuts import render



def home(request):
    return render(request, 'ladingpage.html', {})

def get_started(request):
    return render(request, 'index.html', {})

def get_transactions(request):
    return render(request, 'budgetCategories.html', {})

def get_accounts(request):
    return render(request, 'accounts.html', {})

def get_budget_categories(request):
    return render(request, 'transactions.html', {})

def get_records(request):
    return render(request, 'records.html', {})
