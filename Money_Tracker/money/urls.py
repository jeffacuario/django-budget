from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    # CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,

    # CategoryDeleteView,
    BudgetDetailView,
    # BudgetListView,
    BudgetCreateView,
    BudgetUpdateView,

    TransactionCreateView,
    TransactionUpdateView,

    CardCreateView,
    CardUpdateView,

    HomeListView
    )



urlpatterns = [
    # path('', views.home, name='money-home'),
    path('', HomeListView.as_view(), name='money-home'),
    # path('', auth_views.LoginView.as_view(template_name='money/home.html'), name='login'),
    # path('', BudgetListView.as_view(), name='money-home'),  

    path('budgets/', BudgetCreateView.as_view(), name='budgets-home'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budgets-detail'),
    path('budgets/<int:pk>/update/', BudgetUpdateView.as_view(), name='budget-update'),
    path('budgets/<int:pk>/delete', BudgetCreateView.delete_budget, name='delete_budget'),

    path('settings/cards/', CardCreateView.as_view(), name='money-cards'),
    path('settings/cards/<int:pk>/delete', CardCreateView.delete_card, name='delete_card'),
    path('settings/cards/<int:pk>/update/', CardUpdateView.as_view(), name='cards-update'),

    path('settings/categories/', CategoryCreateView.as_view(), name='money-categories'),
    path('settings/categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='categories-update'),
    path('settings/categories/<int:pk>/delete', CategoryCreateView.delete_category, name='delete_category'), 

    path('<int:pk>/new/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:pk>/delete', BudgetDetailView.delete_transaction, name='delete_transaction'), 
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction-update'),
]
