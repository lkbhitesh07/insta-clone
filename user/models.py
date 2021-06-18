from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures', null=False, blank=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
