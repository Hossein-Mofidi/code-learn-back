from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Role(models.TextChoices):
    student = 'student'
    instructor = 'instructor'
    support = 'support'
    admin = 'admin'


class User(AbstractUser):
    SEX_CHOICES = (
        ('F', 'female'),
        ('M', 'male'),
    )

    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)
    role = models.CharField(max_length=10, choices=Role.choices, default='student', editable=False)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.get_full_name()

    class Meta:
        unique_together = ('phone_number', 'role')