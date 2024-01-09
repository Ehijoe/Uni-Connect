from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User must have an email address")
        
        if not password:
            raise ValueError("User must have a password")
        
        user = self.model(
            email =  self.normalize_email(email),
        )
        user.set_password(password)
        user.is_active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff = True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff = True,
            is_admin = True
        )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True) # login access
    staff = models.BooleanField(default=False) # non-superUser
    admin = models.BooleanField(default=False) # superUser


    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin


class UserProfile(models.Model):
    pass

    # Details for user profile model