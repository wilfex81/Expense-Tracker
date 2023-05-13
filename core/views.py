from django.db.models.functions import TruncMonth

from django.shortcuts import render, redirect

from .models import BudgetCategorie, Account, Transaction
from datetime import datetime
from django.db.models import Sum
from .forms import AccountForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta


def home(request):
    return render(request, 'ladingpage.html', {})


def get_started(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Auth
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in sucessfully")
            return redirect('accounts')
    else:
        return render(request, 'login.html', {})
    return render(request, 'login.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # AUTH and LOGIN
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Sign up was sucessfull')
            return redirect('getstarted')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    return render(request, 'signup.html', {'form': form})


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
        budget_date = datetime.now().date()

        if budget_date_str:
            budget_date = datetime.strptime(budget_date_str, '%B %d, %Y')

        if budget_amount is not None:
            category = BudgetCategorie(name=name,
                                       description=description,
                                       budget_amount=budget_amount,
                                       budget_date=budget_date)
            category.save()
            return redirect('budget_categories')

    categories = BudgetCategorie.objects.all()
    total_budget = '{:,}'.format(
        sum([category.budget_amount for category in categories]))

    context = {
        'categories': categories,
        'total_budget': total_budget,
    }
    return render(request, 'budgetCategories.html', context)


def accounts(request):
    accounts = Account.objects.all().annotate(
        total_balance=Sum('deposited_amount'))
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts')
    else:
        form = AccountForm()
    total_balance = '{:,}'.format(accounts.aggregate(
        sum_balance=Sum('total_balance'))['sum_balance'] or 0)
    return render(request, 'accounts.html', {'form': form, 'accounts': accounts, 'total_balance': total_balance})


@login_required
def transactions(request):
    categories = BudgetCategorie.objects.all()
    accounts = Account.objects.all()
    if request.method == 'POST':
        # Get the form data
        date_recorded = datetime.now().date()
        transaction_date_str = request.POST['budget_date']
        # remove the ', midnight' substring
        transaction_date_str = transaction_date_str.replace(', midnight', '')
        transaction_date = datetime.strptime(
            transaction_date_str, '%B %d, %Y').date()
        cheque_number = request.POST.get('cheque_number', '')
        budget_category_id = request.POST['budget_category']
        budget_category = BudgetCategorie.objects.get(pk=budget_category_id)
        account_id = request.POST['account']

        # Get the description from the selected budget_category
        description = budget_category.description

        # Get the budget_amount from the selected budget_category
        budget_amount = budget_category.budget_amount

        # Create a new transaction object
        transaction = Transaction(
            date_recorded=date_recorded,
            transaction_date=transaction_date,
            description=description,
            cheque_number=cheque_number,
            amount_spent=budget_amount,
            account_id=account_id,
            budget_categorie_id=budget_category_id
        )
        transaction.save()

        # Redirect to the transactions page
        return redirect('records')

    elif request.method == 'GET':
        if request.GET.get('category'):
            category_id = int(request.GET['category'])
            transactions = Transaction.objects.filter(
                budget_categorie__id=category_id)

        transactions = Transaction.objects.all()

        context = {
            'transactions': transactions,
            'categories': categories,
            'accounts': accounts,
        }
        return render(request, 'transactions.html', context)


def records(request):
    # Get the user's account
    account = Account.objects.get(user=request.user)
    # Get the user's transactions for the past year
    year_ago = datetime.now().date() - relativedelta(years=1)
    transactions = Transaction.objects.filter(
        transaction_date__gte=year_ago, account=account)

    # Calculate the total amount spent for each month
    monthly_totals = transactions.annotate(month=TruncMonth('transaction_date')).values(
        'month').annotate(total_amount=Sum('amount_spent')).order_by('month')

    context = {
        'transactions': transactions,
        'monthly_totals': list(monthly_totals),
    }
    return render(request, 'records.html', context)
