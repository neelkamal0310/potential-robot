from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Student(models.Model):
    """
    Model to store student details
    """
    full_name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    mobile_number = models.BigIntegerField(validators=[
        MinValueValidator(1000000000),
        MaxValueValidator(9999999999),
    ])
    guardian_name = models.CharField(max_length=100)
    guardian_number = models.BigIntegerField(validators=[
        MinValueValidator(1000000000),
        MaxValueValidator(9999999999),
    ])
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    batch = models.IntegerField()
    major = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.roll_number} | {self.full_name}'
