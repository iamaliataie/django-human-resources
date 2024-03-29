from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
)
PERSONALITY = (
    ('', 'Select a personality'),
    ('I am outgoing', 'I am outgoing'),
    ('I am sociable', 'I am sociable'),
    ('I am antisocial', 'I am antisocial'),
    ('I am discreet', 'I am discreet'),
    ('I am serious', 'I am serious'),
)
SMOKER = (
    ('1', 'Yes'),
    ('2', 'No'),
)
LANGUAGES = (
    ('Python', 'Python'),
    ('Javascript', 'Javascript'),
    ('C++', 'C++'),
    ('PHP', 'PHP'),
    ('Ruby', 'Ruby'),
    ('Other', 'Other'),
    )
FRAMEWORKS = (
    ('React', 'React'),
    ('Vue', 'Vue'),
    ('Django', 'Django'),
    ('Laravel', 'Laravel'),
    ('RubyOnRails', 'RubyOnRails'),
    ('Other', 'Other'),
    )
DATABASES = (
    ('Mysql', 'Mysql'),
    ('Posgresql', 'Posgresql'),
    ('Mangodb', 'Mangodb'),
    ('Sqlite3', 'Sqlite3'),
    ('Oracle', 'Oracle'),
    ('Other', 'Other'),
)
LIBRARIES = (
    ('Jquery', 'Jquery'),
    ('Chart.js', 'Chart.js'),
    ('Gsap', 'Gsap'),
    ('Graphql', 'Graphql'),
    ('Matplotlib', 'Matplotlib'),
    ('Other', 'Other'),
)
MOBILE = (
    ('React Native', 'React Native'),
    ('Kivy', 'Kivy'),
    ('Flutter', 'Flutter'),
    ('Ionic', 'Ionic'),
    ('Xamarin', 'Xamarin'),
    ('Other', 'Other'),
)
OTHER = (
    ('UML', 'UML'),
    ('SQL', 'SQL'),
    ('Docker', 'Docker'),
    ('GIT', 'GIT'),
    ('Pandas', 'Pandas'),
    ('Other', 'Other'),
)
STATUS_COURSE = (
    ('', 'Select your status'),
    ('I am studying','I am studying'),
    ('I took a break','I took a break'),
    ('Completed','Completed'),
)

class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    # age = models.IntegerField(default=20,)
    birth = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Birthday")
    phone = models.CharField(max_length=25)
    personality = models.CharField(max_length=50, choices=PERSONALITY, null=True)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=50, choices=SMOKER, default="2")
    resume = models.FileField(upload_to='resume', blank=True, verbose_name='Resume')
    image = models.ImageField(upload_to='images', blank=True, verbose_name='Photo')
    messages = models.TextField()
    languages = MultiSelectField(choices=LANGUAGES, default='', max_length=20)
    frameworks = MultiSelectField(choices=FRAMEWORKS, default='', max_length=20)
    databases = MultiSelectField(choices=DATABASES, default='', max_length=20)
    libraries = MultiSelectField(choices=LIBRARIES, default='', max_length=20)
    mobile = MultiSelectField(choices=MOBILE, default='', max_length=20)
    other = MultiSelectField(choices=OTHER, default='', max_length=20)
    # EDUCATION - 3
    institution = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    started_course = models.DateField(auto_now_add=False, auto_now=False)
    finished_course = models.DateField(auto_now_add=False, auto_now=False)
    about_course = models.TextField()
    status_course = models.CharField(max_length=50, null=True, choices=STATUS_COURSE)
    # PROFESSIONAL - 4
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    started_job = models.DateField(auto_now=False, auto_now_add=False)
    finished_job = models.DateField(auto_now=False, auto_now_add=False)
    about_job = models.TextField()
    employed = models.BooleanField(null=True, verbose_name="I am employed")
    remote = models.BooleanField(null=True, verbose_name="I agree to work remotely")
    travel = models.BooleanField(null=True, verbose_name="I am available to travel")
    situation = models.CharField(max_length=20, default='Pending', choices=SITUATION, null=True,)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
    def clean(self) -> None:
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        
    def name(self):
        return self.first_name + ' ' + self.last_name