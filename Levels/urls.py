from django.urls import path
from .views import LevelView

urlpatterns = [
    path('level/<int:user_id>/', LevelView.as_view(), name='level'),
]

