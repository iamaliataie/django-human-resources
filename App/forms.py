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

    about_course = forms.CharField(
        label="About your college course",
        min_length=50,
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'style': 'font-size: 13px',
                'placeholder': 'Talk about your college course',
                'rows': 7,
                'style': 'resize: none;',
            }
        )
    )
    
    about_job = forms.CharField(
        label="About your job",
        min_length=50,
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'style': 'font-size: 13px',
                'placeholder': 'Talk about your last job',
                'rows': 7,
                'style': 'resize: none;',
            }
        )
    )

    company = forms.CharField(
        label="Last company",
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 13px',
                'placeholder': 'Company name',
            }
        )
    )

    position = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 13px',
                'placeholder': 'Your position',
            }
        )
    )

    employed = forms.BooleanField(label="I am employed", required=False)

    remote = forms.BooleanField(label="I agree to work remotely", required=False)

    travel = forms.BooleanField(label="I am available to travel", required=False)

    experience = forms.BooleanField(label='I have experience', required=False)

    class Meta:
        model = Candidate
        # fields = ["first_name", "last_name", "job", "email", 'age', "phone", "messages"]
        exclude = ('situation', 'created_on')
        
        labels = {
            'started_course': 'Started',
            'finished_course': 'Finished',
            'started_job': 'Started',
            'finished_job': 'Finished',
        }
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
                    'max': f'{date.today().year-20}-{date.today().month}-{date.today().day}',
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
                    'min': '1950-01-01',
                    'max': date.today(),
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
                    'min': '1950-01-01',
                    'max': date.today(),
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

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume.content_type != 'application/pdf':
            raise forms.ValidationError('Resume must be PDF')
        return resume

    def clean_birth(self):
        birth = self.cleaned_data.get('birth')
        now = date.today()
        age = (now.year - birth.year) - ((now.month, now.day) < (birth.month, birth.day))
        if age < 20:
            raise forms.ValidationError('Your age must be 20 at least')
        return birth
