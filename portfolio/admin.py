from django.contrib import admin
from .models import *

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = Project.proj_img.through
    extra = 1
    verbose_name = "Project Image"
    verbose_name_plural = "Project Images"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'proj_type')
    list_filter = ('proj_type',)
    inlines = [ProjectImageInline]
    exclude = ('proj_img',)

class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['proj_img_preview']

    def proj_img_preview(self, obj):
        if obj.proj_img:
            return mark_safe(f'<img src="{obj.proj_img.url}" width="100" />')
        return "-"
    proj_img_preview.short_description = "Preview"

from django.utils.safestring import mark_safe     

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(Information)