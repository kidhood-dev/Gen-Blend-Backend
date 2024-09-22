from rest_framework import serializers
from .models import Level
from Users.models import UserProfile

class LevelSerializer(serializers.ModelSerializer):
    is_lock = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = ['id', 'level_name', 'is_lock']

    def get_is_lock(self, obj):
        # Get the user_id from the view context
        user_id = self.context.get('user_id')
        if user_id:
            try:
                # Get the user's profile and current level using the user_id
                user_profile = UserProfile.objects.get(id=user_id)
                current_level = user_profile.current_level
                print(current_level.id)
                # Check if the current level is greater than or equal to the level in question
                return obj.id <= current_level.id  # Levels till current are unlocked

            except UserProfile.DoesNotExist:
                # If user profile doesn't exist, default to locked
                return False
        
        return False  # Default to locked if no user_id or error occurs
