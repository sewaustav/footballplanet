from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name="main"),
    path('events', events, name="events"),
    path('camps', CampsView.as_view(), name='camps'),
    path('tournament', TournamentsView.as_view(), name="tournaments"),
    path('tournament/<int:pk>', TournamentDetailView.as_view(), name="dtour"),
    path('tournament/create-application', create_team, name="application"),
    path('contacts', contacts, name="contacts"),
    path('news', NewsView.as_view(), name="news"),
    path('news/<int:pk>', NewsDetailView.as_view(), name="dnews"),
    path('camps/<int:pk>', CampsDetailView.as_view(), name="dcamp"),
    path('footballfield', footballfield, name="field"),
    path('training', trainingpage, name="training"),
    path('club', clubs, name="club"),
    path('agency', agency, name="agency")

]