from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {"fields": ("username", "password1", "password2")}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                ),  # No 'usable_password'
            },
        ),
        (
            "Personal info",
            {
                "fields": ("name",),  # Include your custom field here
            },
        ),
    )

    # For editing users: Extend default fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (
            "Personal info",
            {
                "fields": ("name",),  # Add custom field
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
