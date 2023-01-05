from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Book


@admin.register(CustomUser,)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','age','address','birth_date','public_visibility')
    list_filter = ('email', 'is_staff', 'is_active','age','address','birth_date','public_visibility')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','age','address','birth_date','public_visibility')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

@admin.register(Book)
class ModelBook(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'cover', 'pdf')
    search_fields = ('author', 'title')
    list_filter = ('category', 'author')
    