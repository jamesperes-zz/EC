from django.contrib import admin
from django.forms import CheckboxSelectMultiple

from .forms import CreateUserForm, UpdateUserFormAdmin
from .models import (ClassRoom, Teacher, Student, Coordinator,
                     Youtube, PdfFile, Class, BasicUser)


class BasicUserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name',
        'email',
    )
    date_hierarchy = 'date_joined'
    search_fields = (
        'first_name', 'last_name', 'email',
        'date_joined',
    )
    list_filter = ('date_joined',)
    add_form = CreateUserForm
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


class YoutubeAdmin(admin.ModelAdmin):
    pass


class PdfFileAdmin(admin.ModelAdmin):
    pass


class ClassRoomAdmin(admin.ModelAdmin):
    pass


class ClassAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(ClassAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['attendances'].widget = CheckboxSelectMultiple()
        return form


class StudentAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


class CoordinatorAdmin(admin.ModelAdmin):
    pass


admin.site.register(BasicUser, BasicUserAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Youtube, YoutubeAdmin)
admin.site.register(PdfFile, PdfFileAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Coordinator, CoordinatorAdmin)