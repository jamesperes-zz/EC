from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)