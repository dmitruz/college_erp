from django.contrib import admin

from .models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "course",
        "exam_type",
        "exam_date",
        "total_marks",
    )

    list_filter = (
        "exam_type",
        "course",
    )

    search_fields = (
        "title",
        "course__course_name",
    )

    ordering = (
        "exam_date",
    )
