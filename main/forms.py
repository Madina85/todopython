
from .models import Habits
from django.forms import ModelForm, fields, TextInput


class HabitsForm(ModelForm):
    class Meta:
        model = Habits
        fields = ['name', 'done_for_today', 'important', 'comment']


        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'План'
            }),
            "done_for_today": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'План действие'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коминтарий'
            }),
            # "important": BooleanInput(attrs={
            #     'class': 'form-control',
                
                
        
        }
