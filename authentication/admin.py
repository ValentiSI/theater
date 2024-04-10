from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'name', 'surname', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('name', 'surname', 'city', 'street', 'apartment', 'phone')}),
        ('Разрешения', {'fields': ('is_staff', 'is_active')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ['email', 'name', 'surname']
    ordering = ['email']


admin.site.register(User, CustomUserAdmin)
