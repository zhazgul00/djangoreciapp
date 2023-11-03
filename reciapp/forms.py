from django.forms import ModelForm
from .models import Room
from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)

class RoomForm(ModelForm):
    class Meta:
        model = Room 
        fields = '__all__'