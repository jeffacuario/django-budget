from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Budget(models.Model):
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50, unique=True)
    categories = models.ManyToManyField(Category)
    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.name

class Card(models.Model):
    cardName = models.CharField(max_length=20, verbose_name='Card Name/Bank Account', unique=True)

    def __str__(self):
        return self.cardName


class Transaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card = models.ForeignKey(Card,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.budget} {self.description} {self.category} {self.amount}"

    def get_absolute_url(self):
        return reverse('budgets-detail', kwargs={'pk':self.budget.id}) # full path of a string


