from django.db import models
from django.conf import settings
from departments.models import Department


class Faculty(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


department = models.ForeignKey(
    Department,
    on_delete=models.PROTECT,
    related_name="faculty_members"
)

    designation = models.CharField(
        max_length=100
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    faculty_id = models.CharField(
    max_length=20,
    unique=True
)

    joining_date = models.DateField()

    phone_number = models.CharField(
        max_length=15
    )

    address = models.TextField()

    profile_picture = models.ImageField(
        upload_to='faculty/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.faculty_id} - {self.user.get_full_name()}"