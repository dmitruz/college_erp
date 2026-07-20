from django.contrib import admin

from .models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "exam",
        "marks_obtained",
        "percentage",
        "letter_grade",
        "is_passed",
    )

    list_filter = (
        "letter_grade",
        "is_passed",
        "exam",
    )

    search_fields = (
        "student__student_id",
        "student__user__first_name",
        "student__user__last_name",
        "exam__title",
    )

    ordering = (
        "-created_at",
    )
