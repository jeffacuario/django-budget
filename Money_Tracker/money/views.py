from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Category, Budget, Transaction, Card
from django.db.models import Sum


# Create your views here.
def home(request):
    return render(request, 'money/home.html')

class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['cardName']
    success_url = '/settings/cards/'

    def get_context_data(self, **kwargs):
        context = super(CardCreateView, self).get_context_data(**kwargs)
        context['card_list'] = Card.objects.all()
        return context
 
    def delete_card(request, pk):
        query = Card.objects.get(id=pk)
        query.delete()
        return redirect("/settings/cards/")   


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['cardName']
    success_url = '/settings/cards/'

    def get_context_data(self, **kwargs):
        context = super(CardUpdateView, self).get_context_data(**kwargs)
        context['card_list'] = Card.objects.all()
        return context



class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'amount']
    success_url = '/settings/categories/'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def delete_category(request, pk):
        query = Category.objects.get(id=pk)
        query.delete()
        # return HttpResponse("<h1>Deleted!</h1>")
        return redirect("/settings/categories/")   



class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name', 'amount']
    success_url = '/settings/categories/'

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        # print(context)
        return context


class BudgetDetailView(LoginRequiredMixin, DetailView):
    model = Budget


    def get_context_data(self, **kwargs):
        context = super(BudgetDetailView, self).get_context_data(**kwargs)

        context['transaction_list'] = Transaction.objects.all()
        context['category_list'] = Category.objects.all()

        total_charges = Transaction.objects.filter(budget=context['budget'].id).aggregate(Sum('amount'))
        if total_charges['amount__sum'] == None:
                total_charges['amount__sum'] = 0

        total_categories = Budget.objects.get(id=context['budget'].id).categories.all().aggregate(Sum('amount'))
        # print(total_categories)

        if total_categories['amount__sum'] == None:
                total_categories['amount__sum'] = 0
        
        sum_list = []
        for each in context['category_list']:
            result = Transaction.objects.filter(budget=context['budget'].id).filter(category=each.id).aggregate(Sum('amount'))
            if result['amount__sum'] == None:
                result['amount__sum'] = 0
            sum_list.append(result)
            result['category'] = each.id

        

        context['sum_list'] = sum_list
        context['total_charges'] = total_charges
        context['total_categories'] = total_categories

        # print(f"\n{context}\n")

        return context

    def delete_transaction(self, pk):
        redirect_string = "/budgets/"
        query = Transaction.objects.get(id=pk)
        redirect_string += str(query.budget.id)
        query.delete()
        return redirect(redirect_string)   




class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    fields = ['name', 'categories']
    success_url = '/budgets'


    def get_context_data(self, **kwargs):
        context = super(BudgetCreateView, self).get_context_data(**kwargs)
        context['budget_list'] = Budget.objects.all()
        return context

    def delete_budget(request, pk):
        query = Budget.objects.get(id=pk)
        query.delete()
        return redirect("/budgets")   


class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    model = Budget
    fields = ['name', 'categories']
    success_url = '/budgets'

    def get_context_data(self, **kwargs):
        context = super(BudgetUpdateView, self).get_context_data(**kwargs)
        context['budget_list'] = Budget.objects.all()
        return context



class TransactionCreateView(LoginRequiredMixin, CreateView):    
    model = Transaction
    fields = ['description', 'amount','card', 'category','note']

    def get_form(self, *args, **kwargs):
        form = super(TransactionCreateView, self).get_form(*args, **kwargs)
        form.fields['category'].queryset = Budget.objects.get(pk=self.kwargs['pk']).categories.all()
        # x = Budget.objects.get(pk=self.kwargs['pk']).categories.all()
        return form

    def form_valid(self, form):
        form.instance.budget = Budget.objects.get(pk=self.kwargs['pk'])
        return super(TransactionCreateView, self).form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = ['date','description', 'amount','card', 'note']

    def get_context_data(self, **kwargs):
        context = super(TransactionUpdateView, self).get_context_data(**kwargs)
        context['transaction_list'] = Transaction.objects.all()
        return context
