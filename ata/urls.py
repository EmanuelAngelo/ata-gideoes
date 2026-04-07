from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AttendanceViewSet,
    ChurchScheduleViewSet,
    MeetingViewSet,
    MemberViewSet,
    MinutesViewSet,
    PartnerChurchViewSet,
)

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'meetings', MeetingViewSet)
router.register(r'minutes', MinutesViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'partner-churches', PartnerChurchViewSet)
router.register(r'church-schedules', ChurchScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
