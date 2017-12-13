from django.contrib import admin
from .forms import CreateUserFormAdmin, UpdateUserFormAdmin
from .models import (User, Calendar, Menssage, ClassRoom, Teacher, Student,
                     Youtube, Pdf_file)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'cod', 'first_name', 'last_name',
        'email', 'type_of_course'
    )
    date_hierarchy = 'date_joined'
    search_fields = (
        'first_name', 'last_name', 'email', 'cod',
        'date_joined', 'type_of_course'
    )
    list_filter = ('type_of_course', 'date_joined',)
    add_form = CreateUserFormAdmin
    form = UpdateUserFormAdmin

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


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
