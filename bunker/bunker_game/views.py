from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import CreateUserForm


def index(request):
    return render(request, 'index.html')


def generate_version(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'generate_version.html')


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
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


def create_tasks(needed_tasks):
    tasks = []

    for key, value in needed_tasks.items():
        for i in range(int(value)):
            tasks.append([f"Условие для {key}_{i}", i])

    return tasks


def created_version(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        fields = ['planimetria', 'vectors', 'stereometry']
        needed_tasks = {field: request.POST.get(field) for field in fields}

        tasks = create_tasks(needed_tasks)

        return render(request, 'created_version.html', {'tasks': tasks})
    else:
        return HttpResponse("Invalid request")


def check_results(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        results = []
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                task_number = key.split('_')[-1]
                user_answer = value
                correct_answer = request.POST.get('correct_answer_' + task_number)
                results.append((user_answer, correct_answer, user_answer == correct_answer))

        return render(request, 'results.html', {'results': results})
    else:
        return HttpResponse("Invalid request")
