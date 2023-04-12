from django.shortcuts import render, redirect

from .models import BudgetCategorie, Account
from datetime import datetime
from django.db.models import Sum
from .forms import AccountForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    return render(request, 'ladingpage.html', {})

def get_started(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Auth
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in sucessfully")
            return redirect('accounts')
    else:
        return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def signup(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #AUTH and LOGIN
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'Sign up was sucessfull')
            return redirect('getstarted')
    else:
        form = SignUpForm()
        return render(request, 'signup.html',{'form' : form})
    return render(request, 'signup.html', {'form' : form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.....')
    return redirect('getstarted')

def budget_categories(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        budget_amount = request.POST.get('budget_amount')
        budget_date_str = request.POST.get('budget_date')
        budget_date = datetime.now()

        if budget_date_str:
            budget_date = datetime.strptime(budget_date_str, '%B %d, %Y, %I:%M %p')
        category = BudgetCategorie(name=name,
                                   description=description,
                                   budget_amount=budget_amount,
                                   budget_date=budget_date)
        category.save()
        return redirect('budget_categories')

    categories = BudgetCategorie.objects.all()
    total_budget = '{:,}'.format(sum([category.budget_amount for category in categories]))

    context = {
        'categories': categories,
        'total_budget': total_budget,
    }
    return render(request, 'budgetCategories.html', context)


def accounts(request):
    accounts = Account.objects.all().annotate(total_balance=Sum('starting_balance'))
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts')
    else:
        form = AccountForm()
    total_balance = '{:,}'.format(accounts.aggregate(sum_balance=Sum('total_balance'))['sum_balance'] or 0)
    return render(request, 'accounts.html', {'form': form, 'accounts': accounts, 'total_balance': total_balance})

def transactions(request):
    return render(request, 'transactions.html', {})

def records(request):
    return render(request, 'records.html', {})
