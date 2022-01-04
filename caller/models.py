from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, name, spam_count, email=None, password=None,):
        """
        Creates and saves a User with the given email, name, phone number and password.
        """
        if not phone_number:
            raise ValueError('Users must have a phone number')

        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            spam_count=spam_count,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, spam_count, email=None, password=None):
        """
        Creates and saves a superuser with the given email, name, phone number and password.
        """
        user = self.create_user(
            phone_number,
            name,
            spam_count,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True,null=True,blank=True)
    phone_number = models.CharField(unique=True, max_length=20)
    spam_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.phone_number)

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


class UnauthUsers(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(unique=True,max_length=20)
    spam_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.phone_number)
