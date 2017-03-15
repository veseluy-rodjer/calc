from django import forms
from .models import Erudmodel

class Addform(forms.ModelForm):
	
    class Meta:
        model = Erudmodel
        fields = ('erud_task', 'erud_answer')