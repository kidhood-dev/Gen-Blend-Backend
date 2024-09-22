from django.urls import path
from .views import *

urlpatterns = [
    path('questions-types/', QuestionsTypeView.as_view(), name='questions_types'),
    path('questions-list/<int:pk>/', QuestionsView.as_view(), name='questions_list'),
    path('question-answer/<int:user_id>', QuestionAnswerCreateAPIView.as_view(), name='question_answer'),

]

