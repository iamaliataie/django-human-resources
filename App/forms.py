from django import forms
from django.core.validators import RegexValidator, integer_validator
from .models import Candidate, SMOKER

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
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'style': 'text-transform: capitalize',
                }
            )
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
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'style': 'text-transform: capitalize',
                }
            )
        )
    job = Uppercase(
        label="Job Code",
        min_length=5,
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'e.g, FR-22',
                'style': 'text-transform: uppercase',
                }
            )
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
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email Address',
                'style': 'text-transform: lowercase',
                }
            )
    )
    age = forms.IntegerField(
        label="Age",
        widget=forms.NumberInput(attrs={'placeholder': 'Age'})
    )
    experience = forms.BooleanField(label='I have experience', required=False)
    messages = forms.CharField(
        label="About You",
        min_length=50,
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Talk a little about yourself', 'rows': 6, 'style': 'resize:none'})
    )
    class Meta:
        model = Candidate
        # fields = ["first_name", "last_name", "job", "email", 'age', "phone", "messages"]
        exclude = ('situation', 'created_on')
        
        SALARY = (
            ('', 'Salary expectation (month)'),
            ('Between  ($3000 and $4000)', 'Between  ($3000 and $4000)'),
            ('Between  ($4000 and $5000)', 'Between  ($4000 and $5000)'),
            ('Between  ($5000 and $7000)', 'Between  ($5000 and $7000)'),
            ('Between  ($7000 and $10000)', 'Between  ($7000 and $10000)'),
        )
        
        GENDER = (
            ('M', 'Male'),
            ('F', 'Female'),
        )
        
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    'placeholder': 'e.g +93 XXXXXXXXX',
                    'data-mask': '(+00) 000-000-0000'
                    }
                ),
            "salary": forms.Select(choices=SALARY),
            "gender": forms.RadioSelect(choices=GENDER),
            "smoker": forms.RadioSelect(choices=SMOKER),
            }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Candidate.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
    
    def clean_age(self):
        age = int(self.cleaned_data.get('age'))
        if age < 20 or age > 50:
            raise forms.ValidationError('Age must be between 20 and 50')
        return age