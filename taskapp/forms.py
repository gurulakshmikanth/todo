from django import forms

from taskapp.models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskList
        fields=['task','done']