from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, MentorProfile, MenteeProfile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MentorProfile)
admin.site.register(MenteeProfile)