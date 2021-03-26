from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "checkout__input"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "checkout__input"}))


class UserRegistrationtionForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"class": "checkout__input"}))
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={"class": "checkout__input"}))

    widgets = {
        'username': forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "checkout__input"})),
        'first_name': forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "checkout__input"})),
        'email': forms.EmailField(widget=forms.EmailInput(attrs={"class": "checkout__input"})),

    }

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
