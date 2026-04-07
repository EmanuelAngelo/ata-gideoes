import django_filters

from .models import Attendance, ChurchSchedule, Meeting, Member, Minutes, PartnerChurch


class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = {
            'status': ['exact'],
            'classification': ['exact'],
            'bond': ['exact'],
            'official_role': ['exact'],
        }


class MeetingFilter(django_filters.FilterSet):
    class Meta:
        model = Meeting
        fields = {
            'status': ['exact'],
            'meeting_type': ['exact'],
            'date': ['exact', 'gte', 'lte'],
            'allow_attendance': ['exact'],
        }


class MinutesFilter(django_filters.FilterSet):
    class Meta:
        model = Minutes
        fields = {
            'status': ['exact'],
            'meeting_id': ['exact'],
            'approval_date': ['exact', 'gte', 'lte'],
        }


class AttendanceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendance
        fields = {
            'meeting_id': ['exact'],
            'member_id': ['exact'],
            'status': ['exact'],
            'member_classification': ['exact'],
        }


class PartnerChurchFilter(django_filters.FilterSet):
    class Meta:
        model = PartnerChurch
        fields = {
            'partnership_status': ['exact'],
            'city': ['exact'],
        }


class ChurchScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = ChurchSchedule
        fields = {
            'status': ['exact'],
            'church_id': ['exact'],
            'church_name': ['exact'],
            'commitment_type': ['exact'],
            'date': ['exact', 'gte', 'lte'],
            'responsible': ['exact'],
        }
