from django.contrib import admin
from .models import Classroom


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):

    list_display = (
        "building",
        "room_number",
        "room_type",
        "capacity",
        "floor",
        "has_projector",
        "has_computers",
        "is_active",
    )

    list_filter = (
        "building",
        "room_type",
        "is_active",
    )

    search_fields = (
        "building",
        "room_number",
    )

    ordering = (
        "building",
        "room_number",
    )