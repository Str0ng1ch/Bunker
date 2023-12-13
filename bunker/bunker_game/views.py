import matplotlib.pyplot as plt
import random
import string

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateUserForm
from .models import Profile

from .all_tasks import task_1


def index(request):
    return render(request, 'index.html', {'active_tab': 'home'})


def generate_version(request):
    return render(request, 'generate_version.html', {'active_tab': 'generate'})


def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user, defaults={'correct': 0, 'incorrect': 0})

    data_list = [1, 2, 3]
    fig, ax = plt.subplots()
    ax.bar(range(len(data_list)), data_list)
    plot_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    fig.savefig(f'bunker_game/static/images/{plot_name}.png')

    context = {
        'user_profile': user_profile,
        'active_tab': 'profile',
        'image_base64': f"{plot_name}.png"
    }
    return render(request, 'accounts/profile.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form, 'active_tab': 'register'}
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

    context = {'active_tab': 'login'}
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
    if request.method == 'POST':
        fields = ['planimetria', 'vectors', 'stereometry']
        needed_tasks = {field: request.POST.get(field) for field in fields}

        # tasks = create_tasks(needed_tasks)
        tasks = [['Площадь треугольника ABC равна 176, DE — средняя линия. Найдите площадь треугольника CDE', 44,
                  'test.svg']]

        return render(request, 'created_version.html', {'tasks': task_1})
    else:
        return HttpResponse("Invalid request")


def check_results(request):
    if request.method == 'POST':
        user_profile, created = Profile.objects.get_or_create(user=request.user,
                                                              defaults={'correct': 0, 'incorrect': 0})
        results, correct, incorrect = [], 0, 0

        for key, value in request.POST.items():
            if key.startswith('answer_'):
                task_number = key.split('_')[-1]
                user_answer = value
                correct_answer = request.POST.get('correct_answer_' + task_number)
                correct += user_answer == correct_answer
                incorrect += user_answer != correct_answer
                results.append((user_answer, correct_answer, user_answer == correct_answer))

        user_profile.correct += correct
        user_profile.incorrect += incorrect
        user_profile.save()

        return render(request, 'results.html', {'results': results})
    else:
        return HttpResponse("Invalid request")
