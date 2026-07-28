from django.contrib import admin

from .models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = (
        "course",
        "exam_type",
        "exam_date",
        "start_time",
        "end_time",
        "semester",
        "academic_year",
    )

    list_filter = (
        "exam_type",
        "semester",
        "academic_year",
    )

    search_fields = (
        "course__course_code",
        "course__course_name",
    )

    ordering = (
        "exam_date",
    )