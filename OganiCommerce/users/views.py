from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserRegistrationtionForm, LoginForm
from store.views import product_list
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return reverse('store:product_list')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationtionForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # login(request, new_user)
            return render(request, 'users/register_done.html', {'new_user': new_user})
        else:
            return HttpResponse('Invalid credentials')
    else:
        user_form = UserRegistrationtionForm()
        return render(request, "users/register.html", {"user_form": user_form})
