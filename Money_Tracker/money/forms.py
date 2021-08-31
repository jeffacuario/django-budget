from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Budget, Transaction


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     # gives us a nested namespace for configurations 
#     # model that will be affected is the User Model
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']

# class NewTransactionForm(forms.ModelForm):
#     # category = forms.ListField()

#     class Meta:
#         model = Transaction
#         fields = ['description', 'amount', 'category', 'note']

#         fields['category'] = Budget.objects.get
