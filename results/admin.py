from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        "enrollment",
        "exam",
        "marks_obtained",
        "letter_grade",
        "is_passed",
        "published_date",
    )

    list_filter = (
        "letter_grade",
        "is_passed",
        "exam",
    )

    search_fields = (
        "enrollment__student__student_id",
        "exam__course__course_name",
    )

    ordering = ("-published_date",)