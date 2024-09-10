from django.urls import path
from .views import *

urlpatterns = [
    path('questions-types/', QuestionsTypeView.as_view(), name='questions-types'),
    path('questions/<int:id>/', QuestionsView.as_view(), name='questions'),
    # path('question-answer/<int:userId>/', QuestionAnswerCreateAPIView.as_view(), name='question-answer'),

]

