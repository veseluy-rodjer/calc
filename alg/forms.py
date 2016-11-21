from django import forms
from .models import Solution

class PostForm(forms.ModelForm):

    class Meta:
        model = Solution
        fields = ('sol',)