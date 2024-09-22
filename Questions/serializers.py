from rest_framework import serializers
from .models import QuestionsType, Questions, QuestionAnswer

class QuestionsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsType
        fields = ['id', 'questions_type']

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'questions_type', 'questions']

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ['question', 'answer', 'user','question_type']
