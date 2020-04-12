from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Team, Appointment

class IndexView(generic.ListView):
    template_name = 'attendance/index.html'
    context_object_name = 'team_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Team.objects.filter().order_by('name')


class DetailView(generic.DetailView):
    model = Team
    template_name = 'attendance/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Team.objects.filter(time_in__lte=timezone.now())


class TeamAppointmentView(generic.ListView):

    template_name = 'attendance/appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        self.team = get_object_or_404(Team, id=self.kwargs['team_id'])
        return Appointment.objects.filter(team=self.team)
        

def AthleteView(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)