from django.contrib import admin
from .models import Cat_org, posts
# Register your models here.

class adminblog(admin.ModelAdmin):
    list_display = (
        "Title", 
        "Time",     
        "Status",
    )
    list_filter = ("Time", "Status",)

admin.site.register(Cat_org)
admin.site.register(posts, adminblog)