from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    

    def __str__(self):
        return self.username


class CV(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    work_experience = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    achievements = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CVs'

    def __str__(self):
        return f"CV of {self.skills} {self.references}"
