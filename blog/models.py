from django.db import models
from accounts.models import User
from django.utils import timezone
from django.utils.html import format_html

# Create your models here.


class Cat_org(models.Model):
    title = models.CharField(max_length=64)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

STATUS_CHOICES = (
        ('v', "ویژه"),
        ('f', "پیش نویس"),
	    ('d', "درانتظار تایید"),
		('p', "منتشر شده"),
	)
class posts(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    Title = models.CharField(max_length=64)
    Body = models.TextField()
    Category = models.ManyToManyField(Cat_org,)
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    Time = models.DateTimeField(default=timezone.now)
    Photo = models.ImageField(upload_to='pic-blog')
    def __str__(self):
        return self.Title
    class Meta:
        verbose_name = "وبلاگ"
        verbose_name_plural = "بلاگ ها"
    def photo_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.Photo.url))
    photo_tag.short_description = "تصویر"	
