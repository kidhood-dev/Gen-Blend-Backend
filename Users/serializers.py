from rest_framework import serializers
from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    mobile_number = serializers.SerializerMethodField('get_mobile_number')
    
    class Meta:
        model = UserProfile
        fields = ['id','mobile_number','name', 'age','gender','current_level']

    def get_mobile_number(self, obj):
        return obj.user.mobile_number
        

class UserProfileResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','name']

from rest_framework import serializers
from .models import UserProfile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile_number']

