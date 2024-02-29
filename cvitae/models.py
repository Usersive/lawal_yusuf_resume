from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user (self, first_name, last_name, username, email, password =None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError('User must have an username')
        
        user = self.model(
            email = self.normalize_email(email),
            username= username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username =username,
            password=password, 
            first_name= first_name,
            last_name=last_name,     
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    objects = MyAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username', 'first_name', 'last_name']
    
    def __str__(self):
        return f'{self.first_name} {self.email}'
    
    def has_perm (self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    def full_name(self):
        return f' {self.first_name} {self.last_name}'


class ProfileUpdate(models.Model):
    first_name      = models.CharField(max_length=50)
    middle_name     = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    image           = models.ImageField(upload_to='profile_images/')
    email           = models.EmailField(max_length=100)
    location        = models.CharField(max_length=50)
    short_bio       = models.CharField(max_length=50)
    bio             = models.TextField(max_length=300)
    objective       = models.TextField(max_length=900)
    
   

    
    def __str__(self):
        return self.email
    
    def full_name(self):
        return f' {self.first_name} {self.last_name} {self.middle_name}'
    
    def firstname(self):
        return self.first_name
     
class PersonalDetail(models.Model):
    date_of_birth   = models.CharField(max_length=20)
    phone_number    = models.CharField(max_length=20)
    gender          = models.CharField(max_length=20)
    marital_status  = models.CharField(max_length=20)
    state           = models.CharField(max_length=30)
    natinality      = models.CharField(max_length=30)
    
    def __str__(self):
        return self.gender
    
class Skill(models.Model):
    skill           = models.CharField(max_length=100)
    skill_percent   = models.IntegerField()
    
    def __str__(self):
        return self.skill
    
class Education(models.Model):
    education_year  = models.CharField(max_length=50)
    education       = models.TextField(max_length=500)
    
    def __str__(self):
        return self.education
    
class Experience(models.Model):
    experience_year   = models.CharField(max_length=20)
    experience      = models.TextField(max_length=200)

class Hobbies(models.Model):
    hobbies         = models.CharField(max_length=100)
    
    def __str__(self):
        return self.hobbies

class SocialLink(models.Model):
    title            = models.CharField(max_length=100)
    url              = models.URLField()
    icon_class       = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class LeadershipRole(models.Model):
    title       = models.CharField(max_length=250)
    department  = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class Professional_member(models.Model):
    title       = models.CharField(max_length=250)
    degree_certificate  = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title

class Project(models.Model):
    program_name       = models.CharField(max_length=50)
    project_title  = models.CharField(max_length=300)
    
    def __str__(self):
        return self.project_title
    
class Portfolio(models.Model):
    title   = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image   = models.ImageField(upload_to='portfolio_images/')
    
    def __str__(self):
        return self.title