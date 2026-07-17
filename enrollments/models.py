from django.db import models
from students.models import Student
from courses.models import Course


class Enrollment(models.Model):

    STATUS_CHOICES = (
        ("active", "Active"),
        ("completed", "Completed"),
        ("dropped", "Dropped"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    academic_year = models.CharField(max_length=9)

    semester = models.PositiveSmallIntegerField()

    enrollment_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    class Meta:
        unique_together = ("student", "course", "academic_year")

    def __str__(self):
        return f"{self.student.student_id} - {self.course.course_code}"
