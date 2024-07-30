from django.contrib import admin
from .models import QuestionsType, Questions, FeedBack

@admin.register(QuestionsType)
class QuestionsTypeAdmin(admin.ModelAdmin):
    """
    Admin interface options for the QuestionsType model.
    
    Displays the ID and question type in the list view.
    """
    list_display = ['id', 'questiontype']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Questions model.
    
    Displays the ID, question type, and question text in the list view.
    """
    list_display = ['id', 'questionstype', 'question']


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    """
    Admin interface options for the FeedBack model.
    
    Displays the ID, question, and answer text in the list view.
    """
    list_display = ['id', 'question', 'answer']
