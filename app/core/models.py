from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self, email, password=None, **extra_fields):
        """ Create a new user profile """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # this is to support musltiple databases
        # we won't use it in this course, bit good to know
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        # extra_fields brauchen wir hier nicht, da wir den superuser in der
        # comandline erstellen
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
