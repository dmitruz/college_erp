from django.db import models

from students.models import Student
from exams.models import Exam


class Grade(models.Model):

    LETTER_GRADES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("F", "F"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="grades"
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="grades"
    )

    marks_obtained = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        editable=False,
        default=0
    )

    letter_grade = models.CharField(
        max_length=2,
        choices=LETTER_GRADES,
        editable=False,
        blank=True
    )

    is_passed = models.BooleanField(
        default=False,
        editable=False
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = ("student", "exam")

    def save(self, *args, **kwargs):

        self.percentage = (
            self.marks_obtained / self.exam.total_marks
        ) * 100

        if self.percentage >= 90:
            self.letter_grade = "A"
        elif self.percentage >= 80:
            self.letter_grade = "B"
        elif self.percentage >= 70:
            self.letter_grade = "C"
        elif self.percentage >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

        self.is_passed = self.percentage >= 60

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.student_id} - {self.exam.title}"
