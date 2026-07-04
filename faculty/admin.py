from django.contrib import admin
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):

    list_display = (
        'faculty_id',
        'user',
        'department',
        'designation',
        'is_active',
    )

    search_fields = (
        'faculty_id',
        'user__username',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'department',
        'is_active',
    )
