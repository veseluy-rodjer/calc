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
            i -= 1
            task_ = Logmodel.objects.all()[i]
            z = i
            return redirect('logica_begin')
        task_ = Logmodel.objects.all()[i]      
        form = LogForm(request.POST)
        if form.is_valid():
            ans = 'Ну-ну...'
            if i > 5:
                ans = 'Быстрее думай!'
            if i > 10:
                ans = 'Еще быстрее!!'
            if i > 15:
                ans = 'Да ты крут!!!'
            sav = form.save(commit=False)
            if sav.log_answer == sav.get_log_sol_display():
                counter += 1
        if i > (len(Logmodel.objects.all()) - 1):
            i -= 1
            task_ = Logmodel.objects.all()[i]
            z = i
            return render(request, 'logica/process.html', {'form':form, 'task_':task_, 'ans':ans, 'c':c, 'x':x, 's':s, 'y':y, 'z':z})
            
            
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

def logica_begin(request):
    return render(request, 'logica/begin.html', {})

def logica_end(request):
    return render(request, 'logica/end.html', {})

def logica_add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddForm()
    return render(request, 'logica/add.html', {'form':form})
