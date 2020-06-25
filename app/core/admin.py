from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# gettext is used for multiple languages support
from django.utils.translation import gettext as _
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    # first we define the sections of our fieldsets in our change
    # and create page
    # None is the title for the section

    fieldsets = ((None, {
        "fields": ('email', 'password')
    }), (_('Personal Info'), {
        'fields': ('name', )
    }), (_('Permissions'), {
        'fields': ('is_active', 'is_staff', 'is_superuser')
    }), (_('Important dates'), {
        'fields': ('last_login', )
    }))
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('email', 'password1', 'password2')
    }), )


admin.site.register(models.User, UserAdmin)
