from django.contrib import admin
from .models import Job, Education

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(Job)

class EducationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Education)
