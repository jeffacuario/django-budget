from django.contrib import admin
from .models import (
    Category,
    Budget, 
    Transaction, 
    Card
    )

# Register your models here.
admin.site.register(Category)
admin.site.register(Budget)
admin.site.register(Transaction)
admin.site.register(Card)

