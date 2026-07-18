from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "course",
        "academic_year",
        "semester",
        "status",
    )

    list_filter = (
        "status",
        "academic_year",
        "semester",
    )

    search_fields = (
        "student__student_id",
        "student__user__first_name",
        "student__user__last_name",
        "course__course_code",
        "course__course_name",
    )

    ordering = (
        "academic_year",
        "semester",
    )