from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, UserProfile
from .serializers import UserProfileSerializer, UserProfileResponseSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from Levels.models import Level
from Coupons.utils import get_coupen

class LoginView(generics.CreateAPIView):
    # serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        mobile_number = request.data.get('mobileNumber')
        try:
            if not mobile_number:
                return Response({'message': 'Mobile number is required'}, status=status.HTTP_400_BAD_REQUEST)
            user, created = User.objects.get_or_create(mobile_number=mobile_number)
            refresh = RefreshToken.for_user(user)
            user_details = UserProfile.objects.filter(user=user)
            user_profile_serializer = UserProfileResponseSerializer(user_details,many=True)
            is_subscribe = get_coupen(user)
            return Response({
                'data':{
                    'authenticationKey':{'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    },
                    'users_list': user_profile_serializer.data,
                    'is_subscribe':is_subscribe
                },
                'status':True,
                'message':'Otp confirmed'
            },status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                'data':{},
                'status':True,
                'message':'Something went wrong.'
            },status=status.HTTP_200_OK)


class UserProflieView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            user_profile = UserProfile.objects.get(pk=pk)

            # Serialize the user profile
            serializer = self.get_serializer(user_profile)

            # Return the serialized profile data in the response
            return Response({
                'data': serializer.data,
                'status': True,
                'message': 'User profile retrieved successfully'
            }, status=status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            # Handle the case where the user does not have a profile
            return Response({
                'data':{},
                'message': 'User profile not found.',
                'status': False
            }, status=status.HTTP_404_NOT_FOUND)
        


class RegisterUserView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        try:
            name = request.data.get('name')
            age = request.data.get('age')
            gender = request.data.get('gender')

            # Get the default level for new users
            level = Level.objects.get(level_name="Level 1")
            
            # Prepare the data for the serializer
            data = {
                "user": request.user.id,  # Pass the user ID or request.user directly depending on the serializer
                "name": name,
                "age": age,
                "gender": gender,
                "current_level": level.id  # Again, pass the level ID or the object itself depending on your serializer
            }

            # Initialize the serializer with the data
            serializer = self.get_serializer(data=data)

            # Validate and save the data
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # Return success response
            return Response({
                'data': serializer.data,
                'status': True,
                'message': 'User profile created successfully'
            }, 
            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'data':{},
                'status':True,
                'message':'Something went wrong.'
            },
            status=status.HTTP_200_OK)