from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Restaurant(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)
    date_of_issue = models.DateField()
    name_of_restaurant = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    # Add related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='restaurants',  # To avoid clashes with auth.User.groups
        blank=True,
        help_text='The groups this restaurant belongs to.',
        related_query_name='restaurant',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='restaurant_permissions',  # To avoid clashes with auth.User.user_permissions
        blank=True,
        help_text='Specific permissions for this restaurant.',
        related_query_name='restaurant',
    )

    def __str__(self):
        return self.name_of_restaurant


class Chef(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
