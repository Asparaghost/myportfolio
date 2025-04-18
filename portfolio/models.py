from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Information(models.Model):
    info_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    email_add = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()
    # resume = models.FileField(upload_to='resume/')
    image = ResizedImageField(force_format="WEBP", quality=100, upload_to='me/')

    class Meta:
        db_table = "personal_information"


class Project(models.Model):
    PERSONAL = 'Personal'
    COMMISSION = 'Commission'

    CHOICE_PROJECT = (
        (PERSONAL, 'Personal'),
        (COMMISSION, 'Commission'),
    )
    proj_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Title")
    tools_used = models.TextField(verbose_name="Tools Used")
    proj_desc = models.TextField(verbose_name="Description")
    scope = models.TextField(verbose_name="Project Scope")
    proj_type = models.CharField(max_length=20, choices=CHOICE_PROJECT, default=COMMISSION, verbose_name="Project Type")
    proj_img = models.ManyToManyField('ProjectImage', blank=True, verbose_name="Project Image(s)")
    year = models.CharField(max_length=4, verbose_name="Year")


    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "projects"


class ProjectImage(models.Model):
    proj_img = ResizedImageField(force_format="WEBP", quality=95, upload_to='proj_images/')

    # def __str__(self):
    #     return self.proj_img.name
    
    class Meta:
        db_table = "project_images"