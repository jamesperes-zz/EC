from django.contrib import admin
from .models import User, Calendar, Menssage, ClassRoom, Teacher


class UserAdmin(admin.ModelAdmin):
    fields = (
        'avatar', 'first_name',
        'last_name', 'email', 'password',
        'cod', 'type_of_course', 'is_active',
        'is_staff', 'attendance', 'grades'
    )
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
