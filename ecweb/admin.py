from django.contrib import admin
from .models import (User, Calendar, Menssage, ClassRoom, Teacher, Student,
                     Youtube, Pdf_file)


class UserAdmin(admin.ModelAdmin):
    pass


class CalendarAdmin(admin.ModelAdmin):
    pass


class MenssageAdmin(admin.ModelAdmin):
    pass


class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1


class YoutubeInline(admin.TabularInline):
    model = Youtube
    extra = 1


class Pdf_fileInline(admin.TabularInline):
    model = Pdf_file
    extra = 1


class TeacherAdmin(admin.ModelAdmin):
    pass


class ClassRoomAdmin(admin.ModelAdmin):
    inlines = [TeacherInline, StudentInline, Pdf_fileInline, YoutubeInline]


admin.site.register(User, UserAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Menssage, MenssageAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)
