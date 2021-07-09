from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserManager

# Create your models here.

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('None', 'Prefer not to say.'),
]

class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures', null=False, blank=False)
    full_name = models.CharField(max_length=100, help_text='Help people discover your account by using the name you\'re known by: either your full name, nickname, or business name.')
    email = models.EmailField(unique=True)

    #optional fields
    bio = models.TextField(blank=True, null=True, help_text='Provide your personal information, even if the account is used for a business, a pet or something else. This won\'t be a part of your public profile.')
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    is_private_account = models.BooleanField(null=True, blank=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
