from django.contrib import admin

from .models import User, UserTask


admin.site.register(User)
admin.site.register(UserTask)
