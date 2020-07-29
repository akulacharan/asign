
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# class to differenciate normal user and a superuser
class UserManager(BaseUserManager):
    # To create a normal user
    def create_user(self,email,mobile,username,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user    =   self.model(
            mobile=mobile,
            email = self.normalize_email(email),
            username = username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # To create a super user,who has all permissions to  access the admin page
    def create_superuser(self,email,mobile,username,password):
        user = self.create_user(
            mobile=mobile,
            email=self.normalize_email(email),
            password = password,
            username=username,

            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Class for creating our desired  fields
class User(AbstractBaseUser):
    mobile          = models.CharField(max_length=40,unique=True)
    email           = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username        = models.CharField(max_length=30,unique=True)
    date_joined     = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login",auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    # This  USERNAME_FIELD  is the main part in this code which is used for login purpose
    USERNAME_FIELD  = 'mobile'

    # The username and password are the inbuilt fields you can also edit according to your requirements
    REQUIRED_FIELDS = ['username','email',]

    # Used to locate the above class(User manager)  for managing users
    objects = UserManager()

    # function returns the string
    def __str__(self):
        return self.email

    # decides the permission of the user
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True












class Customer(models.Model):
    username = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=8)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    passport_num = models.IntegerField()
    image = models.ImageField(upload_to='pics',blank=True)
    password = models.CharField(max_length=20)
    confirm_pasword = models.CharField(max_length=20,blank=True)


    def __str__(self):
        return self.username