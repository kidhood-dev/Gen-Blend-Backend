from rest_framework import serializers
from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField('get_phone_number')
    
    class Meta:
        model = UserProfile
        fields = ['id','phone_number','name', 'age','gender','current_level']

    def get_phone_number(self, obj):
        return obj.user.phone_number
        

class UserProfileResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','name']

from rest_framework import serializers
from .models import UserProfile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']

