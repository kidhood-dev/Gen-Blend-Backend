from rest_framework import generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import QuestionsType, Questions
from .serializers import QuestionsTypeSerializer, QuestionsSerializer, QuestionAnswerSerializer
from rest_framework.response import Response
from Users.models import UserProfile


class QuestionsTypeView(generics.ListAPIView):
    serializer_class = QuestionsTypeSerializer
    authentication_classes = [JWTAuthentication]
    queryset = QuestionsType.objects.all()


class QuestionsView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        id = self.kwargs.get('id')
        return Questions.objects.filter(questionstype=id)


# class QuestionAnswerCreateAPIView(generics.CreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     serializer_class = QuestionAnswerSerializer  

#     def create(self, request, userId, *args, **kwargs):
#         user = UserProfile.objects.get(id=userId)
#         questions_answers_list = request.data.get('questions_answers', [])
#         for question_answer in questions_answers_list:
#             question_answer['user'] = user.id
#         serializer = self.get_serializer(data=questions_answers_list, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Question answers successfully saved."}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
