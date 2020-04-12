from django.contrib import admin
from .models import Team, Athlete, Category, Appointment, Attendance

admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Athlete)
admin.site.register(Appointment)
admin.site.register(Attendance)