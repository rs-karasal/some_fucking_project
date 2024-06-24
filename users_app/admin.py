from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, MentorProfile, MenteeProfile, ManagerProfile, AdminProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'role']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'photo', 'birth_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )


class MentorAdmin(admin.ModelAdmin):
    list_display = ['user']


class MenteeAdmin(admin.ModelAdmin):
    list_display = ['user']


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['user']


class AdminAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MentorProfile, MentorAdmin)
admin.site.register(MenteeProfile, MenteeAdmin)
admin.site.register(ManagerProfile, ManagerAdmin)
admin.site.register(AdminProfile, AdminAdmin)
