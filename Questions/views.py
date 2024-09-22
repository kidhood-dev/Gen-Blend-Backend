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
    
    def list(self, request, *args, **kwargs):
        # Get the filtered queryset
        try:
            queryset = self.get_queryset()

            # Serialize the queryset
            serializer = self.get_serializer(queryset, many=True)

            # Create the custom response structure
            data = [
                {
                    "id": item["id"],
                    "questionsType": item["questions_type"],  # Convert to camelCase manually
                    "questions": item["questions"]
                }
                for item in serializer.data
            ]

            # Return the custom response
            return Response({
                "data": data,
                "status": True,
                "message": "Questions list"
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                "data": {},
                "status": True,
                "message": "Something went wrong."
            }, status=status.HTTP_200_OK)


class QuestionsView(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Questions.objects.filter(questions_type=pk)

    def list(self, request, *args, **kwargs):
        # Get the filtered queryset
        try:
            queryset = self.get_queryset()

            # Serialize the queryset
            serializer = self.get_serializer(queryset, many=True)

            # Create the custom response structure
            data = serializer.data

            # Return the custom response
            return Response({
                "data": data,
                "status": True,
                "message": "Questions list"
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                "data": {},
                "status": True,
                "message": "Something went wrong."
            }, status=status.HTTP_200_OK)


class QuestionAnswerCreateAPIView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = QuestionAnswerSerializer  

    def create(self, request, *args, **kwargs):
        try:
            # Get the user from the request data (using 'userID' as passed in your request)
            user = UserProfile.objects.get(id=kwargs.get('user_id'))
            question_type = QuestionsType.objects.get(id=request.data['questionsType'])
            # Retrieve the list of questions and answers from the request
            questions_answers_list = request.data.get('questionsAnswers', [])
            # Add the user to each question-answer dictionary
            for question_answer in questions_answers_list:
                data = {'question':question_answer['question'],'answer': question_answer['answer'],'user':user.id, 'question_type': question_type.id}
                serializer = self.get_serializer(data=data)
                # Validate the data
                if serializer.is_valid():
                    # Save the data
                    serializer.save()
            return Response({
                "data": {},
                "status": True,
                "message": "Question answers successfully saved."
            }, status=status.HTTP_200_OK) 
        except Exception as e:
            return Response({
                "data": {},
                "status": False,
                "message": "Something went wrong"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)