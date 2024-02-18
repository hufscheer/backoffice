from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Member(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    organization = models.ForeignKey('Organization', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=255)
    is_manager = models.BooleanField()
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'members'