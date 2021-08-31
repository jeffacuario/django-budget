from django.contrib import admin
from django.urls import path
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
    CardUpdateView
    )


urlpatterns = [
    # path('', views.home, name='money-home'),
    # path('', BudgetListView.as_view(), name='money-home'),  


    path('<int:pk>/', BudgetDetailView.as_view(), name='budgets-detail'),
    path('', BudgetCreateView.as_view(), name='money-home'),
    path('<int:pk>/update/', BudgetUpdateView.as_view(), name='budget-update'),
    path('<int:pk>/delete', BudgetCreateView.delete_budget, name='delete_budget'),

    path('cards/', CardCreateView.as_view(), name='money-cards'),
    path('cards/<int:pk>/delete', CardCreateView.delete_card, name='delete_card'),
    path('cards/<int:pk>/update/', CardUpdateView.as_view(), name='cards-update'),

    path('categories/', CategoryCreateView.as_view(), name='money-categories'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='categories-update'),
    path('categories/<int:pk>/delete', CategoryCreateView.delete_category, name='delete_category'), 


    path('transaction/<int:pk>/delete', BudgetDetailView.delete_transaction, name='delete_transaction'), 
    path('<int:pk>/new/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction-update'),
]
