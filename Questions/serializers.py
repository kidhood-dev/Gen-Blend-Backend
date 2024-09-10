from rest_framework import serializers
from .models import QuestionsType, Questions, QuestionAnswer

class QuestionsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsType
        fields = ['id', 'questiontype']

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'questionstype', 'question']

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ['question', 'answer','user']