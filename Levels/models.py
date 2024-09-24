from django.db import models
from core.models import BaseModel

class Level(BaseModel):
    """
    Represents a game level with a name, maximum score, and minimum score.
    
    Attributes:
        level_name (str): The name of the level.
        max_score (int, optional): The maximum score achievable in the level.
        min_score (int, optional): The minimum score required to pass the level.
    """
    level_name = models.CharField(max_length=50)
    max_score = models.IntegerField(blank=True, null=True)
    min_score = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        """
        Returns a string representation of the Level object.
        
        Returns:
            str: The name of the level.
        """
        return self.level_name


class Score(BaseModel):
    """
    Represents a score achieved by a user in a specific level.
    
    Attributes:
        user (ForeignKey): The user who achieved the score.
        level (ForeignKey): The level in which the score was achieved.
        score (int, optional): The score achieved by the user.
        max_score (int, optional): The maximum score achieved by the user.
    """
    user = models.ForeignKey("Users.UserProfile", related_name="user_scores", on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name="level_scores", on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True)
    max_score = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the Score object.
        
        Returns:
            str: The score achieved by the user.
        """
        return str(self.score)


class LevelAttempt(BaseModel):
    """
    Represents an attempt made by a user to complete a specific level.
    
    Attributes:
        user (ForeignKey): The user attempting the level.
        level (ForeignKey): The level being attempted.
        total_attempt_count (int, optional): The total number of attempts made by the user.
        attempts_to_unlock_next_level (int, optional): The number of attempts required to unlock the next level.
    """
    user = models.ForeignKey("Users.UserProfile", related_name="user_level_attempts", on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name="level_attempts", on_delete=models.CASCADE)
    total_attempt_count = models.IntegerField(blank=True, null=True)
    attempts_to_unlock_next_level = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        """
        Returns a string representation of the LevelAttempt object.
        
        Returns:
            str: The name of the level being attempted.
        """
        return self.level.level_name
