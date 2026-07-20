from django.db import models

from courses.models import Course


class Exam(models.Model):

    EXAM_TYPES = (
        ("assignment", "Assignment"),
        ("quiz", "Quiz"),
        ("midterm", "Midterm"),
        ("final", "Final Exam"),
        ("practical", "Practical"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="exams"
    )

    title = models.CharField(max_length=100)

    exam_type = models.CharField(
        max_length=20,
        choices=EXAM_TYPES
    )

    total_marks = models.PositiveIntegerField(default=100)

    exam_date = models.DateField()

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.course_code} - {self.title}"
