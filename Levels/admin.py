from django.contrib import admin
from .models import Level, LevelAttempt, Score

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Level model.
    
    Displays the ID, level name, minimum score, and maximum score in the list view.
    """
    list_display = ['id', 'level_name', 'min_score', 'max_score']


@admin.register(LevelAttempt)
class LevelAttemptAdmin(admin.ModelAdmin):
    """
    Admin interface options for the LevelAttempt model.
    
    Displays the ID, user, level, score, and maximum score in the list view.
    """
    list_display = ['id', 'user', 'level', 'total_attempt_count', 'attempts_to_unlock_next_level']


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Score model.
    
    Displays the ID, user, level, total attempt count, and attempts to unlock the next level in the list view.
    """
    list_display = ['id', 'user', 'level', 'score', 'max_score']
