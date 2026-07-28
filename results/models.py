from django.db import models
from enrollments.models import Enrollment
from exams.models import Exam


class Result(models.Model):

    LETTER_GRADES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("F", "F"),
    )

    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="results"
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="results"
    )

    marks_obtained = models.PositiveIntegerField()

    letter_grade = models.CharField(
        max_length=2,
        choices=LETTER_GRADES
    )

    is_passed = models.BooleanField(default=True)

    feedback = models.TextField(
        blank=True
    )

    published_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("enrollment", "exam")

    def __str__(self):
        return (
            f"{self.enrollment.student.student_id} - "
            f"{self.exam.exam_type} - "
            f"{self.letter_grade}"
        )