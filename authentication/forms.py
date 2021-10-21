from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# Form value we will recieve from the login page for verification.
class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = {'full_name', 'email', 'username', 'password1', 'password2'}

# For admin pannel incase we want to change some values of user.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = {'full_name', 'email', 'username'}
