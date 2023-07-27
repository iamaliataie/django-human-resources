from django.db import models

# Create your models here.

SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
)

class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    age = models.IntegerField(default=20,)
    phone = models.CharField(max_length=25)
    messages = models.TextField()
    situation = models.CharField(max_length=20, default='Pending', choices=SITUATION, null=True,)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
    def clean(self) -> None:
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()