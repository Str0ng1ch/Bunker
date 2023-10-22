from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


def index(request):
    return render(request, 'index.html')


def register_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username, password = request.POST.get('username'), request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
