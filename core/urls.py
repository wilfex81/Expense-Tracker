from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('getStarted/', views.get_started, name = 'getstarted'),
    path('transactions/', views.get_transactions, name = 'transactions'),
    path('accounts/', views.get_accounts, name = 'accounts'),
    path('budgetCategories/', views.get_budget_categories, name = 'budget_categories'),
    path('records/', views.get_records, name = 'records'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)