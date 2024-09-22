from django.urls import path
from .views import LoginView,  RegisterUserView, UserProflieView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('user-profile/<int:pk>/', UserProflieView.as_view(), name='user_profile'),
    path('register-user/', RegisterUserView.as_view(), name='register_user'),
]

