# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Organization, UserOrganization

User = get_user_model()


class UserOrganizationInline(admin.TabularInline):
    model = UserOrganization
    extra = 0


class UserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'is_staff']

    ordering = ['email']
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "usable_password", "password1", "password2"),
            },
        ),
    )
    inlines = [UserOrganizationInline]


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    inlines = [UserOrganizationInline]


admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
