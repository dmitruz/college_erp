from django.db import models
# from enrollments.models import Enrollment


# class Attendance(models.Model):

#     STATUS_CHOICES = (
#         ("present", "Present"),
#         ("absent", "Absent"),
#         ("late", "Late"),
#         ("excused", "Excused"),
#     )

#     enrollment = models.ForeignKey(
#         Enrollment,
#         on_delete=models.CASCADE,
#         related_name="attendance_records"
#     )

#     date = models.DateField()

#     status = models.CharField(
#         max_length=10,
#         choices=STATUS_CHOICES
#     )

#     remarks = models.TextField(
#         blank=True
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     class Meta:
#         ordering = ["-date"]
#         unique_together = ("enrollment", "date")

#     def __str__(self):
#         return (
#             f"{self.enrollment.student.student_id} - "
#             f"{self.enrollment.course.course_code} - "
#             f"{self.date}"
#         )