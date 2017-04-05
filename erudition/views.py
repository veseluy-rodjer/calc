# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Erudmodel
import time
from .forms import Addform, Erudform

# Create your views here.

i = 0
a = time.time()
counter = 0

def erudition_add(request):
    if request.method == "POST":
        form = Addform(request.POST)
        if form.is_valid():
            form.save()
    form = Addform()
    return render(request, 'erudition/add.html', {'form':form})

def start_erudition(request):
    return render(request, 'erudition/start_erudition.html', {})

def erudition_process1(request):
    global i
    global a
    global counter
    i = 0
    a = time.time()
    counter = 0
    return redirect('erudition_process')

def erudition_process(request):
    global i
    global a
    global counter
    task_ = Erudmodel.objects.all()[i]
    if request.method == "POST":
        form = Erudform(request.POST)
        if form.is_valid():
            ans = 'Осталось ' + str(len(Erudmodel.objects.all()) - i - 1) + ' задач'
            sav = form.save(commit=False)
            string = Erudmodel.objects.get(pk=i+1)
            string.erud_sol = sav.erud_sol
            string.save()
            if Erudmodel.objects.all()[i].erud_answer == sav.erud_sol:
                counter += 1
        i += 1
        if i > len(Erudmodel.objects.all()) - 1:
            return redirect('erudition_result')        
        task_ = Erudmodel.objects.all()[i]
    else:
        ans = ''
    form = Erudform()
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
        return redirect('erudition_end')
    return render(request, 'erudition/process.html', {'form':form, 'task_':task_, 'ans':ans, 'c':c, 'x':x, 's':s, 'y':y})

def erudition_end(request):
    return render(request, 'erudition/end.html', {})

def erudition_result(request):
    global counter
    if counter <= 5:
        appraisal = 'Очевидно, ты очень умный, но ответы нажимал наугад.'
    elif 5 < counter <=10:
        appraisal = 'Не очень хорошо, надо тренировать свой мозг'
    elif 10 < counter <= 15:
        appraisal = 'Хорошо, но ты можешь лучше.'
    elif 15 < counter <= 16:
        appraisal = 'Очень хороший результат! Ты почти великолепен!'
    else:
        appraisal = 'Отличный результат! Ты лучший!'
    slip = Erudmodel.objects.all()
    return render(request, 'erudition/result.html', {'counter':counter, 'appraisal':appraisal, 'slip':slip})