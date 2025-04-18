from django.contrib import admin
from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'proj_type')
    list_filter = ('proj_type',)  

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Information)