from django.db import models
from core.models import BaseModel

class QuestionsType(BaseModel):
    """
    Represents a type of question in the feedback system.
    
    Attributes:
        questiontype (str): The type or category of the question.
    """
    questiontype = models.CharField(max_length=255)

    def __str__(self) -> str:
        """
        Returns a string representation of the QuestionsType object.
        
        Returns:
            str: The type of the question.
        """
        return self.questiontype

class Questions(BaseModel):
    """
    Represents a specific question in the feedback system.
    
    Attributes:
        questionstype (ForeignKey): The type of the question.
        question (str): The text of the question.
    """
    questionstype = models.ForeignKey(QuestionsType, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)

    def __str__(self) -> str:
        """
        Returns a string representation of the Questions object.
        
        Returns:
            str: The text of the question.
        """
        return self.question

class FeedBack(BaseModel):
    """
    Represents a feedback response to a specific question.
    
    Attributes:
        question (ForeignKey): The question being answered.
        answer (str): The text of the feedback answer.
    """
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=10000)

    def __str__(self) -> str:
        """
        Returns a string representation of the FeedBack object.
        
        Returns:
            str: The text of the answer.
        """
        return self.answer