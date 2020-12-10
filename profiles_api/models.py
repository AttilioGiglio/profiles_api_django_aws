from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionMixin 

class UserProfile(AbstractBaseUser, PermissionMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # for custom manager, to control users
    objects = UserProfileManager()

    # to work with admin and user django system, so here it specify that the used needs a email and name to login
    USER_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    #  to retrive the full name user. Self is always used with classes as first attribute
    def get_full_name(self):
    """ Retrieve full name of user """
        return self.name
    
    def get_short_name(self):
    """ Retrieve short name of user """
        return self.name

    # String representation of model
    def __str__(self):
    """ Return string representation of our user """
        # So it will be represented the model with email
        return self.email



