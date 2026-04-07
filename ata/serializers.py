from rest_framework import serializers

from .models import Attendance, ChurchSchedule, Meeting, Member, Minutes, PartnerChurch


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class MinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minutes
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class PartnerChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerChurch
        fields = '__all__'


class ChurchScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchSchedule
        fields = '__all__'
