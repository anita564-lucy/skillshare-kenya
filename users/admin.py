from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserCreationForm, UserChangeForm
from .models import User, ProviderProfile, SeekerProfile


class ProviderProfileInline(admin.StackedInline):
    model = ProviderProfile
    can_delete = False
    verbose_name_plural = "Provider Profile"


class SeekerProfileInline(admin.StackedInline):
    model = SeekerProfile
    can_delete = False
    verbose_name_plural = "Seeker Profile"


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ("email", "first_name", "last_name", "type", "gender", "is_staff", "is_active")
    list_filter = ("type", "gender", "is_active", "is_staff")

    fieldsets = (
        (_("Credentials"), {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name", "gender")}),
        (_("Permissions"), {"fields": ("is_staff", "is_active", "is_verified", "is_superuser", "groups", "user_permissions")}),
        (_("User Type"), {"fields": ("type",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "gender", "password1", "password2", "type", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    def get_inlines(self, request, obj=None):
        if obj:
            if obj.type == User.Types.PROVIDER:
                return [ProviderProfileInline]
            elif obj.type == User.Types.SEEKER:
                return [SeekerProfileInline]
        return []


admin.site.register(User, CustomUserAdmin)


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__email",)


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__email",)