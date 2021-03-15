from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("User Detail", {
            "fields": (
                "avatar",
                "gender",
                "bio",
                "birthday",
                "age",
                "status",
            ),
        }),
    )

    list_filter = UserAdmin.list_filter + ('status', 'gender',)

    list_display = ('username',
                    'email',
                    'first_name',
                    'last_name',
                    'gender',
                    'age',
                    'status',
                    )