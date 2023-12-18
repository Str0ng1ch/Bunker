import random
import string

import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateUserForm
from .models import Attempt
from .tasks import tasks, themes

matplotlib.use('Agg')


def index(request):
    return render(request, 'index.html', {'active_tab': 'home'})


def repeat_form(request):
    return render(request, 'repeat_form.html')


def reference_materials(request):
    return render(request, 'reference_materials.html', {'active_tab': 'reference_materials'})


def generate_version(request):
    return render(request, 'generate_version.html', {'active_tab': 'generate'})


def get_attempts_data(attempts):
    data, all_correct, all_incorrect = [], 0, 0

    for attempt in attempts:
        all_correct += attempt.correct
        all_incorrect += attempt.incorrect
        data.append(attempt.correct / (attempt.correct + attempt.incorrect))

    return data, all_correct, all_incorrect


def crop_top_pixels(plot_name):
    image = Image.open(f'bunker_game/static/images/{plot_name}.png')
    width, height = image.size
    cropped_image = image.crop((0, 50, width, height - 20))

    cropped_image.save(f'bunker_game/static/images/{plot_name}.png')


def make_profile_graph(data, length):
    plot_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

    plt.bar(range(len(data)), data, color='orange')
    plt.xticks(range(len(data)), [f'Попытка {i + length + 1}' for i in range(len(data))])
    plt.ylim(0, 1)

    plt.savefig(f'bunker_game/static/images/{plot_name}.png')
    plt.close()

    crop_top_pixels(plot_name)

    return plot_name


def profile(request):
    attempts = Attempt.objects.filter(user=request.user)
    data, correct, incorrect = get_attempts_data(attempts)

    plot_name = make_profile_graph(data[-5:], len(data))

    context = {
        'active_tab': 'profile',
        'graph': f"{plot_name}.png",
        'correct': correct,
        'incorrect': incorrect
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


def create_tasks(needed_tasks, tasks_type):
    ready_tasks, count = [], 0

    for key, value in needed_tasks.items():
        if tasks_type or int(value) > 0:
            ready_tasks.extend(random.sample(tasks[key], 1 if tasks_type else int(value)))
    return ready_tasks


def created_version(request):
    if request.method == 'POST':
        request.session['form_key'] = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        request.session[f'form_{request.session["form_key"]}_submitted'] = 0

        needed_tasks = {theme: request.POST.get(theme) for theme in themes}
        tasks_type = True if 'create_full_version' in request.POST else False

        ready_tasks = create_tasks(needed_tasks, tasks_type)
        request.session['tasks'] = ready_tasks

        return render(request, 'created_version.html', {'tasks': ready_tasks})
    else:
        return HttpResponse("Invalid request")


def check_results(request):
    if request.method == 'POST':
        if request.session[f'form_{request.session["form_key"]}_submitted'] == 1:
            return redirect('repeat_form')
        request.session[f'form_{request.session["form_key"]}_submitted'] = 1

        results, correct, incorrect = [], 0, 0
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                task_number = key.split('_')[-1]
                user_answer = value
                correct_answer = request.POST.get('correct_answer_' + task_number)
                correct += user_answer == correct_answer
                incorrect += user_answer != correct_answer
                results.append((user_answer, correct_answer, user_answer == correct_answer))

        if request.user.is_authenticated:
            attempt = Attempt.objects.create(user=request.user, correct=correct, incorrect=incorrect)
            attempt.save()

        return render(request, 'results.html', {'results': results, 'tasks': request.session['tasks']})
    else:
        return HttpResponse("Invalid request")

# TODO решение с решу егэ
