from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from register.models import User


class UserAdmin(UserAdmin):
    exclude = ('username',)
    list_display = (
        'email',
        'first_name',
        'last_name',
        'middle_name',
        'date_joined',
        'last_login',
        'is_admin',
        'is_staff',
    )
    search_fields = (
        'email',
        'id',
    )
    readonly_fields = (
        'id',
        'date_joined',
        'last_login',
    )
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
