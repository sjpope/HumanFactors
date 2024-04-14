from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *


admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(ReservationSlot)


class DiningProfileInline(admin.StackedInline):
    model = DiningProfile
    can_delete = False
    verbose_name_plural = 'dining profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (DiningProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)