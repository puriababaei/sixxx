from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.site_header = "داشبورد مدیریت وب اپلیکیشن"

UserAdmin.fieldsets[2][1]['fields'] = (
										'phone',
										'id_telegram',
										'id_instagram',
										'avatar',
										'is_active', 
										'is_staff', 
										'is_superuser', 
										'vip_author', 
										'groups', 
										'user_permissions'
									)
UserAdmin.list_display += ('vip_author', 'is_staff', 'phone')

admin.site.register(User, UserAdmin)