from django.contrib import admin
from .models import User, UserProfile

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    """
    Admin interface options for the User model.

    Attributes:
        list_display (list): Fields to display in the admin list view.
    """
    list_display = ['id', 'email', 'mobile_number', 'is_subscribed']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface options for the UserDetail model.

    Attributes:
        list_display (list): Fields to display in the admin list view.
    """
    list_display = ['id', 'user', 'name', 'age', 'gender', 'current_level']
