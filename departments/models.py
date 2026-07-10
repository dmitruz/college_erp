from django.db import models
from departments.models import Department


class Department(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True
    )

    name = models.CharField(
          Department,
        on_delete=models.PROTECT,
        related_name="faculty_members"
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.code} - {self.name}"