from django.contrib import admin
from .models import Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    list_display = (
        "course",
        "department",
        "faculty",
        "academic_year",
        "semester",
        "class_type",
        "day",
        "start_time",
        "end_time",
        "classroom",
    )

    list_filter = (
        "academic_year",
        "semester",
        "department",
        "class_type",
        "day",
    )

    search_fields = (
        "course__course_name",
        "course__course_code",
        "faculty__faculty_id",
        "classroom__room_number",
    )

    ordering = (
        "day",
        "start_time",
    )