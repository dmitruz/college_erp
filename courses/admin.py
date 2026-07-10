from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'course_code',
        'course_name',
        'department',
        'semester',
        'faculty',
        'credits',
        'is_active',
    )

    list_filter = (
        'department',
        'semester',
        'is_active',
    )

    search_fields = (
        'course_code',
        'course_name',
    )

    ordering = ('course_code',)