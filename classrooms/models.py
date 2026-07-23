from django.db import models


class Classroom(models.Model):

    ROOM_TYPES = (
        ("Lecture", "Lecture Hall"),
        ("Lab", "Computer Lab"),
        ("Seminar", "Seminar Room"),
        ("Workshop", "Workshop"),
    )

    building = models.CharField(
        max_length=100
    )

    room_number = models.CharField(
        max_length=20
    )

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES
    )

    capacity = models.PositiveIntegerField()

    floor = models.PositiveSmallIntegerField()

    has_projector = models.BooleanField(default=False)

    has_computers = models.BooleanField(default=False)

    has_whiteboard = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["building", "room_number"],
                name="unique_room"
            )
        ]

        ordering = [
            "building",
            "room_number",
        ]

    def __str__(self):
        return f"{self.building} - {self.room_number}"