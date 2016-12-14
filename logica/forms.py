from django import forms
from .models import Logmodel

class LogForm(forms.ModelForm):

    class Meta:
        model = Logmodel
        fields = ('log_sol',)
        widgets = {'log_sol':forms.RadioSelect}


class AddForm(forms.ModelForm):
	
    class Meta:
        model = Logmodel
        fields = ('log_task', 'log_answer')