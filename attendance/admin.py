from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "enrollment",
        "date",
        "status",
    )

    list_filter = (
        "status",
        "date",
    )

    search_fields = (
        "enrollment__student__student_id",
        "enrollment__course__course_code",
    )