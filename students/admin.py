from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'student_id',
        'user',
        'phone_number',
        'admission_date',
        'is_active',
    )

    search_fields = (
        'student_id',
        'user__username',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'gender',
        'is_active',
    )
