from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from authentication.forms import UserForm, CustomUserChangeForm

User = get_user_model()

# Register your models here.

# Our custom user admin model
class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = ( # fields we have to specify for a new user to enter
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('bio', 'website')}),
    )
    fieldsets = ( # fields we have to specify for change some property of user
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('bio', 'website')}),
    )

admin.site.register(User, CustomUserAdmin)
