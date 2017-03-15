# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Logmodel
import time
from .forms import AddForm, LogForm

# Create your views here.

i = 0
a = time.time()
counter = 0

def logica_process(request):
    global i
    global a
    global counter
    task_ = Logmodel.objects.all()[i]
    if request.method == "POST":
        i += 1
        if i > len(Logmodel.objects.all()) - 1:
            return redirect('logica_result')
        task_ = Logmodel.objects.all()[i]      
        form = LogForm(request.POST)
        if form.is_valid():
            ans = 'aaa', len(Logmodel.objects.all()) - i, 'sss'
            sav = form.save(commit=False)
            if Logmodel.objects.all()[i - 1].log_answer == sav.get_log_sol_display():
                counter += 1
    else:
        ans = ''
    form = LogForm()
    c = 300 - int(time.time() - a)
    x = 0
    y = 0
    s = 'Осталось времени'
    if c > 59:
        y = c // 60
        c = c % 60
    if y > 9:
        x = y // 10
        y = y % 10
    if c < 1 and x == 0 and y == 0:
        a = time.time()
        i = 0
        return redirect('logica_end')
    return render(request, 'logica/process.html', {'form':form, 'task_':task_, 'ans':ans, 'c':c, 'x':x, 's':s, 'y':y})

def start_logica(request):
    return render(request, 'logica/start_logica.html', {})

def logica_process1(request):
    global i
    global a
    global counter
    i = 0
    a = time.time()
    counter = 0
    return redirect('logica_process')

def logica_end(request):
    return render(request, 'logica/end.html', {})

def logica_add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddForm()
    return render(request, 'logica/add.html', {'form':form})

def logica_result(request):
    global counter
    if counter <= 5:
        appraisal = 'Очевидно, ты очень умный, но ответы нажимал наугад.'
    elif 5 < counter <=10:
        appraisal = 'Не очень хорошо, надо тренировать свой мозг'
    elif 10 < counter <= 15:
        appraisal = 'Хорошо, но ты можешь лучше'
    elif 15 < counter <= 17:
        appraisal = 'Очень хороший результат! Ты почти великолепен!'
    else:
        appraisal = 'Отличный результат! Ты лучший!'
    return render(request, 'logica/result.html', {'counter':counter, 'appraisal':appraisal})