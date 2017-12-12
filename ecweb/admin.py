from django.contrib import admin
from .models import User, Calendar, Menssage, ClassRoom, Teacher


class UserAdmin(admin.ModelAdmin):
    pass


class CalendarAdmin(admin.ModelAdmin):
    pass


class MenssageAdmin(admin.ModelAdmin):
    pass


class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1


class TeacherAdmin(admin.ModelAdmin):
    pass


class ClassRoomAdmin(admin.ModelAdmin):
    inlines = [TeacherInline]


admin.site.register(User, UserAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Menssage, MenssageAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)
