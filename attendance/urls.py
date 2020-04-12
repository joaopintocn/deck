from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:team_id>/details', views.DetailView.as_view(), name='details'),
    path('<int:team_id>/appointments', views.TeamAppointmentView.as_view(), name='appointments'),
    path('<int:pk>/athletes', views.AthleteView, name='athletes'),   
]
