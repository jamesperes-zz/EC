from django.contrib import admin
from .models import User, Calendar, Menssage, ClassRoom


class UserAdmin(admin.ModelAdmin):
    pass


class CalendarAdmin(admin.ModelAdmin):
    pass

class MenssageAdmin(admin.ModelAdmin):
    pass

class ClassRoomAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Menssage, MenssageAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)