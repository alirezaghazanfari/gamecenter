from django.contrib import admin
from web.models.user import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
