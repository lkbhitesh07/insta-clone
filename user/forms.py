from django import forms
from django.forms import fields
from django.contrib.auth import get_user_model

User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'picture',
            'full_name',
            'username',
            'email',
            'bio',
            'website',
            'phone_number',
            'gender',
            'is_private_account',
        )

        labels = {
            'is_private_account': 'Do you want to make your account private ?',
            'phone_number': 'Phone'
        } #labels to give name in particular