from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from authentication.forms import UserForm, CustomUserChangeForm

User = get_user_model()

# Register your models here.

# We have to create a custom admin model as we have created our custom user model, so to show it properly in admin pannel according to us we will create
# custom admin model

class CustomUserAdmin(UserAdmin):
    add_form = UserForm # to create new user we need form - In case we want to create a user from admin
    form = CustomUserChangeForm # when we want to change some setting from user than we have to make a custom user with details
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
