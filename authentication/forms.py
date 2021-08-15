from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = {'full_name', 'email', 'username', 'password1', 'password2'}

class CustomUserChangeForm(UserChangeForm): #For admin pannel incase we want to change some values of user.
    class Meta:
        model = get_user_model()
        fields = {'full_name', 'email', 'username'}
