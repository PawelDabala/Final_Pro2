from django import forms
from .models import Car, Customer

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = '__all__'
        exclude = ['rents']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['rents']

class HwLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)