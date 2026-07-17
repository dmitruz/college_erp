from django.db import models
from django.conf import settings
from departments.models import Department


class Student(models.Model):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    student_id = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="students"
    )

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    phone_number = models.CharField(
        max_length=15
    )

    address = models.TextField()

    admission_date = models.DateField()

    profile_picture = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_id} - {self.user.get_full_name()}"
