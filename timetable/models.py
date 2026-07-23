from django.db import models
from departments.models import Department
from courses.models import Course
from faculty.models import Faculty
from classrooms.models import Classroom


class Timetable(models.Model):

    DAYS = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
    )

    CLASS_TYPES = (
        ("Lecture", "Lecture"),
        ("Lab", "Lab"),
        ("Tutorial", "Tutorial"),
        ("Seminar", "Seminar"),
    )

    SEMESTER_CHOICES = (
        (1, "Semester 1"),
        (2, "Semester 2"),
        (3, "Semester 3"),
        (4, "Semester 4"),
        (5, "Semester 5"),
        (6, "Semester 6"),
        (7, "Semester 7"),
        (8, "Semester 8"),
    )


    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="timetables"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="timetables"
    )

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="timetables"
    )

    academic_year = models.CharField(
        max_length=9,
        help_text="Example: 2026/2027"
    )

    semester = models.PositiveSmallIntegerField(
        choices=SEMESTER_CHOICES
    )

    class_type = models.CharField(
        max_length=20,
        choices=CLASS_TYPES
    )

    day = models.CharField(
        max_length=10,
        choices=DAYS
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    classroom = models.ForeignKey(
    Classroom,
    on_delete=models.PROTECT,
    related_name="timetables",
    null=True,
    blank=True
)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["day", "start_time"]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "academic_year",
                    "semester",
                    "department",
                    "day",
                    "start_time",
                    "classroom",
                ],
                name="unique_room_schedule"
            ),
            models.UniqueConstraint(
                fields=[
                    "academic_year",
                    "semester",
                    "faculty",
                    "day",
                    "start_time",
                ],
                name="unique_faculty_schedule"
            ),
        ]

    def __str__(self):
        return (
            f"{self.course.course_code} | "
            f"{self.day} | "
            f"{self.start_time}"
        )