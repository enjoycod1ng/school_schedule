from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Schedule
from .serializers import ScheduleSerializer
from django.utils.timezone import now


class ScheduleListView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        for_today = self.request.query_params.get("for_today", None)
        class_name = self.request.query_params.get("class_name", None)

        if for_today:
            today = now().isoweekday()
            queryset = queryset.filter(day_of_week=today)

        if class_name:
            queryset = queryset.filter(school_class__name=class_name)

        return queryset
