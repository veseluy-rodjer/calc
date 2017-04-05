# -*- coding: utf-8 -*-
from django import forms
from .models import Humormodel

class Addform(forms.ModelForm):
	
    class Meta:
        model = Humormodel
        fields = ('humor_task',)
        
