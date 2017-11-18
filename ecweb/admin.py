from django.contrib import admin
from .models import User, Calendar


class UserAdmin(admin.ModelAdmin):
    pass


class CalendarAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Calendar, CalendarAdmin)
