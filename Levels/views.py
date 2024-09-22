from rest_framework import generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Level
from .serializers import LevelSerializer

class LevelView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LevelSerializer
    queryset = Level.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            # Extract user_id from the URL
            user_id = kwargs.get('user_id')

            # Get all levels
            queryset = self.get_queryset()

            # Serialize the queryset, passing the user_id into the context
            serializer = self.get_serializer(queryset, many=True, context={'user_id': user_id})

            # Return the serialized data
            return Response({
                'data': serializer.data,
                'status': True,
                'message': 'Levels retrieved successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': False,
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
