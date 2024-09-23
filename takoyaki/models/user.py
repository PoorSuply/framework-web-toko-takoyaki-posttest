from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    BUYER = 1
    ADMIN = 2
    ROLE_CHOICES = (
        (BUYER, 'Buyer'),
        (ADMIN, 'Admin'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=BUYER)

    def __str__(self):
        return self.username
