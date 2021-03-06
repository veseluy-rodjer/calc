# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Solution
from .forms import PostForm, AddForm
import time

# Create your views here.

i = 0
a = time.time()

def process(request):
    global i
    global a
    task_ = Solution.objects.all()[i].task
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            got = form.save(commit=False)
            got.task = task_
            got.resh()
            if got.sol == got.answer:
                form = PostForm()
                ans = 'Молодец!'
                i += 1
                if i > (len(Solution.objects.all()) - 1):
                    i = 0
                    a = time.time()
                    return redirect('begin')
                task_ = Solution.objects.all()[i].task
            else:
                form = PostForm()
                ans = 'Да ты двоечник!'
    else:
        form = PostForm()
        ans = ''
    c = 60 - int(time.time() - a)
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
        return redirect('end')
    return render(request, 'alg/process.html', {'form':form, 'task_':task_, 'ans':ans, 'c':c, 'x':x, 's':s, 'y':y})
	
def process1(request):
    global i
    global a
    i = 0
    a = time.time()
    return redirect('process')

def addd(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddForm()
    return render(request, 'alg/addd.html', {'form':form})

def begin(request):
    return render(request, 'alg/begin.html', {})

def end(request):
    return render(request, 'alg/end.html', {})

def start_alg(request):
    return render(request, 'alg/start_alg.html', {})

def head(request):
    return render(request, 'alg/head.html', {})

