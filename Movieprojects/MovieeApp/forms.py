from django import forms
from .models import Movies

class Moviesform(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','Desc','year','img']