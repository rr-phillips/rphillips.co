from django.contrib import admin
from .models import *

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Projects)

class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(Job)

class EducationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Education)