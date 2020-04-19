from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AttendanceConfig(AppConfig):
    name = 'attendance'

    def ready(self):
        import attendance.signals