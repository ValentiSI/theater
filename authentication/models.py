from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=255, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=255, blank=True, verbose_name='Фамилия')
    phone = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Телефон')
    email = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Email')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = _("пользователь")
        verbose_name_plural = _("пользователи")

    def __str__(self):
        return self.email
    