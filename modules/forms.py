from django import forms
from django.forms import ModelForm, TextInput, EmailInput,Textarea
from .models import Feedback
from django.core import validators

class FeedbackForm(forms.ModelForm):
    min=2
    max=50
    msg_min = f"Should have atleast {min} char"
    msg_max = f"Should have maximum {max} char"
    regex="^[A-Za-z]+(?: [A-Za-z]+)*$"
    name_warning='The name accepts only letters!'
    email = forms.EmailField(validators=[validators.validate_email])
    name = forms.CharField(validators=[
        validators.MinLengthValidator(min, msg_min),
        validators.MaxLengthValidator(max, msg_max),
        validators.RegexValidator(regex, name_warning)
        ])
    

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name',
                'style':'input w-96 py-4 '
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'placeholder': 'Email',
                'style':'input input-bordered w-full max-w-xs'
                }),
            'message': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Message',
                'style':'textarea textarea-bordered'
                })    
        }