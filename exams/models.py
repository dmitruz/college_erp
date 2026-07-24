from django.db import models

from courses.models import Course


class Exam(models.Model):

    EXAM_TYPES = (
        ("Midterm", "Midterm"),
        ("Final", "Final"),
        ("Quiz", "Quiz"),
        ("Practical", "Practical"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="exams"
    )

    exam_type = models.CharField(
        max_length=20,
        choices=EXAM_TYPES
    )

    exam_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    total_marks = models.PositiveIntegerField()

    passing_marks = models.PositiveIntegerField()

    academic_year = models.CharField(
        max_length=9
    )

    semester = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.course_code} - {self.exam_type}"