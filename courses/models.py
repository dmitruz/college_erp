from django.db import models
from faculty.models import Faculty
from departments.models import Department


class Course(models.Model):


    SEMESTER_CHOICES = (
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
        (7, 'Semester 7'),
        (8, 'Semester 8'),
    )

    course_code = models.CharField(
        max_length=10,
        unique=True
    )

    course_name = models.CharField(
        max_length=100
    )

    department = models.CharField(
        Department,
    on_delete=models.PROTECT,
    related_name="courses"
    )

    semester = models.PositiveSmallIntegerField(
        choices=SEMESTER_CHOICES
    )

    credits = models.PositiveSmallIntegerField()

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses'
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"
