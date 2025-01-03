from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User

class UserAuth(BaseBackend):
    def authenticate(self, request, username=None, email=None, password=None):
        """
        Authenticate a user based on email (or username) and password.
        """
        try:
            if email:
                user = User.objects.get(email=email)  # Try to find by email
            elif username:
                user = User.objects.get(username=username)  # Fallback to username if no email
            else:
                return None  # If neither email nor username is provided, return None

        except User.DoesNotExist:
            return None

        # Check the password
        if check_password(password, user.password):
            return user

        return None

    def get_user(self, user_id):
        """
        Retrieve a user instance by their primary key (ID in this case).
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

