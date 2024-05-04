from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from app.users.models import User


@admin.register(User)
class UserAdmins(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    (
                        "first_name",
                        "last_name",
                    ),
                    "show_contact_info",
                    "current_state",
                    "avatar",
                    "description",
                    "email",
                    "mobile",
                    (
                        "last_login",
                        "date_joined",
                    ),
                )
            },
        ),
        (
            _("User Permission"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )

    readonly_fields = [
        "last_login",
        "date_joined",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ["id", "username", "mobile", "first_name", "last_name"]
    search_fields = ["username", "first_name", "last_name", "mobile"]
