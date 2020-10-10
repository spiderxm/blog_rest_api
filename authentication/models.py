from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    """Manager to manage the creation of users"""

    def create_user(self, email, name, password):
        """To create a user from his credentials"""
        if email:
            user = User(email=email, name=name)
            user.set_password(password)
            user.save()
            return user
        else:
            raise ValueError("User Must Have an email address")

    def create_superuser(self, email, name, password):
        """To create super user from his details"""
        user = self.create_user(email=email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    To manage new users
    """
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """Returns email as representation of the object"""
        return self.email
