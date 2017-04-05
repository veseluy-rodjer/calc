# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Humormodel
from .forms import Addform

# Create your views here.

i = 0
counter = 0

def start_humor(request):
    return render(request, 'humor/start_humor.html', {})

def start_process(request):
    global i
    global counter
    i = 0
    counter = 0
    task_ = Humormodel.objects.all()[i]
    ans = ''
    return render(request, 'humor/process.html', {'task_':task_, 'ans':ans})

def humor_process(request, v):
    vv = int(v)
    global i
    global counter
    ans = 'Осталось ' + str(len(Humormodel.objects.all()) - i - 1) + ' задач'
    i += 1
    counter += vv
    if i > len(Humormodel.objects.all()) - 1:
        return redirect('humor_result')        
    task_ = Humormodel.objects.all()[i]
    return render(request, 'humor/process.html', {'task_':task_, 'ans':ans})
    
def humor_result(request):
    global counter
    if 10 <= counter < 18:
        appraisal = 'Даже в хорошем настроении ты слишком практичен, трезв в суждениях, а это никого не развеселит, скорее утомит окружающих.'
    elif 18 <= counter < 27:
        appraisal = 'Ты обладаешь здоровым, реальным чувством юмора, в шутках не перебарщиваешь. Твое остроумие не задевает и не утомляет окружающих.'
    else:
        appraisal = 'Юмор в тебе просто бурлит. Даже перехлестывает через края. Так что будь посдержаннее, иначе твое поведение можно истолковать не так, как тебе бы хотелось.'
    return render(request, 'humor/result.html', {'appraisal':appraisal})
    
def humor_add(request):
    if request.method == "POST":
        form = Addform(request.POST)
        if form.is_valid():
            form.save()
    form = Addform()
    return render(request, 'humor/add.html', {'form':form})
