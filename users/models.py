from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Moderator', 'Moderator'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Add custom related_name
        blank=True
    )