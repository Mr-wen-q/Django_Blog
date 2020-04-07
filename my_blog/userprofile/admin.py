from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'UserProfile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# 重新注册
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

