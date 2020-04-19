from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Team, Athlete, Category, Appointment, Attendance

# Define an inline admin descriptor for Athlete model
# which acts a bit like a singleton
class AthleteInline(admin.StackedInline):
    model = Athlete
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (AthleteInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Athlete)
admin.site.register(Appointment)
admin.site.register(Attendance)