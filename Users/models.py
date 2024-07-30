from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from Levels.models import Level

class CustomUserManager(BaseUserManager):
    """
    Custom manager for User model.

    Methods:
        create_user: Creates and saves a User with the given email and mobile number.
        create_superuser: Creates and saves a superuser with the given email and mobile number.
    """
    def create_user(self, email, mobile_number, password=None):
        """
        Creates and saves a User with the given email, mobile number, and password.
        
        Args:
            email (str): The email address of the user.
            mobile_number (str): The mobile number of the user.
            password (str, optional): The password for the user. Defaults to None.
        
        Returns:
            User: The created user object.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            mobile_number=mobile_number,
        )
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile_number, password=None):
        """
        Creates and saves a superuser with the given email, mobile number, and password.
        
        Args:
            email (str): The email address of the superuser.
            mobile_number (str): The mobile number of the superuser.
            password (str, optional): The password for the superuser. Defaults to None.
        
        Returns:
            User: The created superuser object.
        """
        user = self.create_user(
            email,
            mobile_number=mobile_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """
    A custom User model that extends AbstractBaseUser.
    
    Attributes:
        email (EmailField): User's email address.
        mobile_number (CharField): User's mobile number.
        is_subscribed (BooleanField): Indicates if the user is subscribed to any service.
        is_active (BooleanField): Indicates if the user account is active.
        is_admin (BooleanField): Indicates if the user has admin privileges.
        is_staff (BooleanField): Indicates if the user can access the admin site.
    """
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=10)
    is_subscribed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_number']

    objects = CustomUserManager()

    def __str__(self) -> str:
        """
        Returns the string representation of the user, which is the mobile number.

        Returns:
            str: The user's mobile number.
        """
        return self.mobile_number
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

class UserProfile(BaseModel):
    """
    A model that stores additional details about a user.
    
    Attributes:
        MALE (str): Constant for the male gender.
        FEMALE (str): Constant for the female gender.
        GENDER_CHOICES (tuple): Choices for gender field.
        user (ForeignKey): Reference to the associated User.
        name (CharField): User's name.
        age (IntegerField): User's age.
        gender (CharField): User's gender with choices restricted to GENDER_CHOICES.
        current_level (ForeignKey): User's current level.
    """
    MALE = "male"
    FEMALE = "female"
    
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    user = models.ForeignKey(User, related_name="user_profiles", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, default=MALE, max_length=15)
    current_level = models.ForeignKey(Level, related_name="current_levels", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        """
        Returns the string representation of the user profile, which is the user's name.

        Returns:
            str: The user's name.
        """
        return self.name
