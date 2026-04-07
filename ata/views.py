from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .filters import (
	AttendanceFilter,
	ChurchScheduleFilter,
	MeetingFilter,
	MemberFilter,
	MinutesFilter,
	PartnerChurchFilter,
)
from .models import Attendance, ChurchSchedule, Meeting, Member, Minutes, PartnerChurch
from .serializers import (
	AttendanceSerializer,
	ChurchScheduleSerializer,
	MeetingSerializer,
	MemberSerializer,
	MinutesSerializer,
	PartnerChurchSerializer,
)


class BaseViewSet(viewsets.ModelViewSet):
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	ordering = ['-created_date']
	ordering_fields = '__all__'


class MemberViewSet(BaseViewSet):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer
	filterset_class = MemberFilter
	search_fields = ['full_name', 'email', 'phone', 'field', 'created_by']


class MeetingViewSet(BaseViewSet):
	queryset = Meeting.objects.all()
	serializer_class = MeetingSerializer
	filterset_class = MeetingFilter
	search_fields = ['title', 'location', 'leader', 'bible_reading', 'created_by']
	ordering = ['-date', '-created_date']


class MinutesViewSet(BaseViewSet):
	queryset = Minutes.objects.all()
	serializer_class = MinutesSerializer
	filterset_class = MinutesFilter
	search_fields = ['meeting_title', 'full_text', 'signers', 'created_by']


class AttendanceViewSet(BaseViewSet):
	queryset = Attendance.objects.all()
	serializer_class = AttendanceSerializer
	filterset_class = AttendanceFilter
	search_fields = ['member_name', 'member_role', 'observations', 'created_by']


class PartnerChurchViewSet(BaseViewSet):
	queryset = PartnerChurch.objects.all()
	serializer_class = PartnerChurchSerializer
	filterset_class = PartnerChurchFilter
	search_fields = ['name', 'pastor_name', 'city', 'email', 'phone', 'created_by']
	ordering = ['name', '-created_date']


class ChurchScheduleViewSet(BaseViewSet):
	queryset = ChurchSchedule.objects.all()
	serializer_class = ChurchScheduleSerializer
	filterset_class = ChurchScheduleFilter
	search_fields = ['church_name', 'pastor_name', 'responsible', 'city', 'observations', 'created_by']
	ordering = ['-date', '-created_date']
