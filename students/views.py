from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        "department",
        "gender",
        "is_active",
    ]

    search_fields = [
        "student_id",
        "user__first_name",
        "user__last_name",
    ]

    ordering_fields = [
        "student_id",
        "admission_date",
        "created_at",
    ]

    ordering = ["student_id"]