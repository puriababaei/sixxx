from django.db import models
from django.utils import timezone
# Create your models here.


class Cat_org(models.Model):
    title = models.CharField(max_length=64)
    def __str__(self):
        return self.title

STATUS_CHOICES = (
        ('v', "ویژه"),
        ('f', "پیش نویس"),
	    ('d', "درانتظار تایید"),
		('p', "منتشر شده"),
	)
class posts(models.Model):
    Title = models.CharField(max_length=64)
    Body = models.TextField()
    Category = models.ManyToManyField(Cat_org,)
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    Time = models.DateTimeField(default=timezone.now)
    Photo = models.ImageField(upload_to='pic-blog')
    def __str__(self):
        return self.Title