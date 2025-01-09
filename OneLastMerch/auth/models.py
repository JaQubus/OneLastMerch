from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator

# Custom user manager to handle user creation
class CustomUserManager(BaseUserManager):
    # Method to create a user with the specified username, email, and password
    def create_user(self, username, email, password=None):
        # Ensure that an email address is provided
        if not email:
            raise ValueError("The Email field must be set")
        
        # Normalize the email to lowercase for consistency
        email = self.normalize_email(email)
        
        # Create a new user using custom model
        user = self.model(email=email, username=username)
        
        # Set the user's password securely (hashes it internally)
        user.set_password(password)
        
        # Save the user to the database using the database from settings (default one)
        user.save(using=self._db)
        
        return user

# Custom user model that replaces Django's default user model
# i wanted to create my own user model, altough i knew there is a Django User model already done. I thought it would give me less magic-like programming experience
class User(AbstractBaseUser):
    # Primary key for the User model (automatically increments), tried to use email. Django hates non-integer primary keys.
    id = models.BigAutoField(primary_key=True, null=False)
    
    # Email field with uniqueness and indexing for efficient lookups, and so when adding more features it won't need the entire database to be redone
    email = models.EmailField(unique=True, db_index=True)
    
    # Username field
    username = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        unique=True
    )

    # Specifies which field will be used as the unique identifier for authentication
    # because I wanted it that way 
    USERNAME_FIELD = 'email'
    
    # Fields required in addition to the USERNAME_FIELD when creating a user
    # well i thought it may be needed
    REQUIRED_FIELDS = ['username']

    # Specifies the custom manager for this model
    # custom create user
    objects = CustomUserManager()

