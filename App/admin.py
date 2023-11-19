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
        'job',
        'birth',
        'phone',
        'personality',
        'salary',
        'gender',
        'experience',
        'smoker',
        'resume',
        'image',
        'messages',
        'languages',
        'frameworks',
        'databases',
        'libraries',
        'mobile',
        'other',
        'institution',
        'course',
        'started_course',
        'finished_course',
        'about_course',
        'status_course',
        'company',
        )
    exclude = ('status',)
    list_filter = ('situation',)
    list_display = ('name', 'email', 'created_on', 'status', '_')
    search_fields = ('first_name', 'last_name', 'email',)
    

    fieldsets = [
        ('PERSONAL', {'fields': ['first_name', 'last_name', 'birth' ,'email', 'phone', 'gender', 'personality', 'smoker', 'image', 'messages',]}),
        ('Skills', {'fields': ['languages', 'frameworks', 'databases', 'libraries', 'mobile', 'other',]}),
        ('Education', {'fields': ['institution', 'course', 'started_course', 'finished_course', 'about_course', 'status_course',]}),
        ('Professional', {'fields': ['company', 'position', 'started_job', 'finished_job', 'about_job', 'employed', 'remote', 'travel',]}),
    ]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.remove('first_name')
            fields.remove('last_name')
        return fields
    
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