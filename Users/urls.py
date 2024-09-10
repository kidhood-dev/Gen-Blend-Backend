from django.urls import path
from .views import UserDetailsView,  RegisterUserView

urlpatterns = [
    path('user-details/', UserDetailsView.as_view(), name='user_details'),
    path('register-user/', RegisterUserView.as_view(), name='register_user'),
]

