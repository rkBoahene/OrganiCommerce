from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'address', 'postal_code', 'city']
    widgets = {
        'first_name': forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "checkout__input"})),
        'last_name': forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "checkout__input"})),
        'email': forms.EmailField(widget=forms.EmailInput(attrs={"class": "checkout__input"})),
        'address': forms.CharField(max_length=250, widget=forms.TextInput(attrs={"class": "checkout__input"})),
        'postal_code': forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "checkout__input"})),
        'city': forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "checkout__input"})),
    }
