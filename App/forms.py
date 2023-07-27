from django import forms
from django.core.validators import RegexValidator, integer_validator
from .models import Candidate

class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

class CandidateForm(forms.ModelForm):
    
    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        validators=[
                RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message='Only letters are allowed'),
                ],
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        validators=[
                RegexValidator(
                    r'^[a-zA-ZÀ-ÿ\s]*$',
                    message='Only letters are allowed'
                    )
                ],
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    job = Uppercase(
        label="Job Code",
        min_length=5,
        max_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'e.g FR-22'})
    )
    email = Lowercase(
        label="Email Address",
        max_length=100,
        validators=[
                RegexValidator(
                    r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
                    message='Enter a valid email address'
                    )
                ],
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'})
    )
    age = forms.IntegerField(
        label="Age",
        min_value=20,
        widget=forms.NumberInput(attrs={'placeholder': 'Age'})
    )
    messages = forms.CharField(
        label="About You",
        max_length=255,
        widget=forms.Textarea(attrs={'placeholder': 'Talk a little about yourself (255 characters)', 'rows': 6, 'style': 'resize:none'})
    )
    class Meta:
        model = Candidate
        fields = ["first_name", "last_name", "job", "email", 'age', "phone", "messages"]
        
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    'placeholder': 'e.g +93 XXXXXXXXX',
                    'data-mask': '(+00) 000-000-0000'
                    }
                )
            }