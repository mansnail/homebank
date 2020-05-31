from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import UserProfile


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',
                    'password_expired', 'email_confirmed')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'password_expired')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'email_confirmed')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gender', 'birthday', 'avatar')


admin.site.register(get_user_model(), UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
