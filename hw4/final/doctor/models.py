from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, phone, password=None, user_type=None):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, phone=phone, user_type=user_type)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, phone, user_type=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            phone=phone,
            user_type=1
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class BaseUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'doctor'),
        (2, 'patient'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    phone = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'password']


class Spec(models.Model):
    name = models.CharField(max_length=200)


class Doctor(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
    number = models.IntegerField()
    online_pay = models.BooleanField()
    expeerience_year = models.IntegerField()
    address = models.TextField()
    rate = models.FloatField()
    rate_num = models.IntegerField(default=0)
    week_days = ArrayField(models.BooleanField(default=False))


class Patient(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)


class Comment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    comment = models.TextField()
