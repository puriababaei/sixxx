from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=12, verbose_name="شماره تماس")
    avatar = models.ImageField(upload_to="avatar", verbose_name="تصویر پروفایل")
    id_telegram = models.URLField(default="https://t.me/", verbose_name="تلگرام ID")
    id_instagram = models.URLField(default="https://instagram.com/", verbose_name="اینستاگرام ID")
    vip_author = models.BooleanField(default=False, verbose_name="💎")
