from datetime import date
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
    # age = forms.IntegerField(
    #     label="Age",
    #     widget=forms.NumberInput(attrs={'placeholder': 'Age'})
    # )
    experience = forms.BooleanField(label='I have experience', required=False)
    messages = forms.CharField(
        label="About You",
        min_length=50,
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Talk a little about yourself', 'rows': 6, 'style': 'resize:none'})
    )

    resume = forms.FileField(
        label="Resume",
        widget=forms.ClearableFileInput(
            attrs={
                'style': 'font-size: 13px',
            }
        )
    )
    image = forms.FileField(
        label="Photo",
        widget=forms.ClearableFileInput(
            attrs={
                'style': 'font-size: 13px',
            }
        )
    )
    institution = forms.CharField(
        label="Institution",
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 13px',
                'placeholder': 'Institution name',
            }
        )
    )
    course = forms.CharField(
        label="Course",
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 13px',
                'placeholder': 'College name',
            }
        )
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
            "birth":forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'onkeypress': 'return false;',
                    'min': '1950-01-01',
                    'max': '2003-01-01',
                }
            ),
            "started_course":forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'onkeypress': 'return false;',
                    'min': '1950-01-01',
                    'max': date.today(),
                }
            ),
            "finished_course":forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'onkeypress': 'return false;',
                }
            ),
            "started_job":forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'onkeypress': 'return false;',
                    'min': '1950-01-01',
                    'max': date.today(),
                }
            ),
            "finished_job":forms.DateInput(
                attrs={
                    'style': 'font-size: 13px; cursor: pointer;',
                    'type': 'date',
                    'onkeypress': 'return false;',
                }
            ),
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