from django.contrib import admin
from django.utils.html import format_html

from .models import Candidate
from .forms import CandidateForm

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    form = CandidateForm
    readonly_fields = (
        'created_on',
        'first_name',
        'last_name',
        'email',
        'age',
        'job',
        'personality',
        'experience',
        'phone',
        'salary',
        'gender',
        'smoker',
        'resume',
        'messages',
        'languages',
        'frameworks',
        'databases',
        'libraries',
        'mobile',
        'other',
        )
    exclude = ('status',)
    list_filter = ('situation',)
    list_display = ('first_name', 'last_name', 'email', 'created_on', 'status', '_')
    search_fields = ('first_name', 'last_name', 'email', 'age',)
    
    # function to change the icon for the status of the candidate
    def _(self, obj):
        if obj.situation == 'Approved':
            return True
        elif obj.situation == 'Rejected':
            return False
        else:
            return None
    _.boolean = True
    
    
    # function to set the color of the status text
    def status(self, obj):
        if obj.situation == 'Approved':
            color = 'green'
        elif obj.situation == 'Rejected':
            color = 'red'
        else:
            color = 'orange'
        
        return format_html('<strong style="color:{}">{}</strong'.format(color, obj.situation))

admin.site.register(Candidate, CandidateAdmin)