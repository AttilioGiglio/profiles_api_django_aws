from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Database model for users in the system"""
    # Doc string """"""
    # If the password is not give it, It will assign value None, that It will throw an error 
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have an email address')
        # Normalize the email address, so the email it will be lower case.
        email = self.normalize_email(email)
        # create the model for this class
        user = self.model(email=email, name=name)
        # hash the password
        user.set_password(password)
        # saving object class to BD and support on different DBs
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user =self.create_user(email, name, password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # for custom manager, to control users
    objects = UserProfileManager()

    # to work with admin and user django system, so here it specify that the used needs a email and name to login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    #  to retrive the full name user. Self is always used with classes as first attribute
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    # String representation of model
    def __str__(self):
        """Return string representation of our user"""
        # So it will be represented the model with email
        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # tell to django what to do if a user is deleted, so with cascade it delete all the data related to that user
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text