# -*- coding: utf-8 -*-
from django import forms
from .models import Erudmodel

class Addform(forms.ModelForm):
	
    class Meta:
        model = Erudmodel
        fields = ('erud_task', 'erud_answer')

class Erudform(forms.ModelForm):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = [(a, 'вариант a'), (b, 'вариант b'), (c, 'вариант c'), (d, 'пропустить вопрос')]
    erud_sol = forms.ChoiceField(label='', choices=e, widget=forms.RadioSelect)
    
    class Meta:
        model = Erudmodel
        fields = ('erud_sol',)
 