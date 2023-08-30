from django.shortcuts import render, redirect
from .forms import UserForm, AccountForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    userForm = UserForm()
    accountForm = AccountForm()
    if request.method == "POST":
        userForm = UserForm(request.POST)
        accountForm = AccountForm(request.POST)
        if userForm.is_valid() and accountForm.is_valid():
            userForm_obj = userForm.save()
            account_obj = accountForm.save(commit=False)
            account_obj.user = userForm_obj
            account_obj.save()
            messages.success(request, 'Account Create Successfully')

    return render(request, "signup.html", context={"userForm": userForm, "accountForm": accountForm})


def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
    return render(request, "login.html", context={"form": form})


@login_required(login_url="login")
def logout_user(request):

    logout(request)
    return redirect("home")
