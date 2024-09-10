from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, UserProfile
from .serializers import UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from Levels.models import Level


class UserDetailsView(generics.CreateAPIView):
    # serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        mobile_number = request.data.get('mobileNumber')
        try:
            if not mobile_number:
                return Response({'message': 'Mobile number is required'}, status=status.HTTP_400_BAD_REQUEST)
            user, created = User.objects.get_or_create(mobile_number=mobile_number)
            refresh = RefreshToken.for_user(user)
            userDetails = UserProfile.objects.filter(user=user)
            userProfileSerializer = UserProfileSerializer(userDetails,many=True)
            return Response({
                'authenticationKey':{'refresh': str(refresh),
                'access': str(refresh.access_token),
                },
                'usersList': userProfileSerializer.data
            },status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        

class RegisterUserView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        try:
            name = request.data.get('name')
            age = request.data.get('age')
            gender = request.data.get('gender')
            level = Level.objects.get(level_name = "Level 1")
            UserProfile.objects.create(user=request.user,name=name,age=age,gender=gender,current_level=level)
            return Response({'message': 'User Created'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
