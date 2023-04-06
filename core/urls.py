from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('getStarted/', views.get_started, name = 'getstarted'),
    path('transactions/', views.transactions, name = 'transactions'),
    path('accounts/', views.accounts, name = 'accounts'),
    path('budgetCategories/', views.budget_categories, name = 'budget_categories'),
    path('records/', views.records, name = 'records'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)