from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *
from itertools import chain

# Create your views here.

def main_page(request):
    current_datetime = datetime.now()
    upcoming_tournaments = Tournaments.objects.filter(start_date__gte=current_datetime).order_by('start_date')[:3]
    upcoming_football_camps = FootballCamp.objects.filter(start_date__gte=current_datetime).order_by('start_date')[:3]
    events = sorted(
        chain(upcoming_tournaments, upcoming_football_camps),
        key=lambda event: event.start_date
    )[:3]
    news = NewsFootball.objects.all()

    context = {
        'events': events,
        'news': news,
    }
    return render(request, 'content/main.html', context)

def trainingpage(request):
    return render(request, 'content/training.html')

def clubs(request):
    return render(request, 'content/club.html')

def footballfield(request):
    return render(request, 'content/footballfield.html')

def agency(request):
    return render(request, 'content/agency.html')

def events(request):
    latest_tournaments = Tournaments.objects.order_by('-start_date')[:3]
    latest_camps = FootballCamp.objects.order_by('-start_date')[:3]

    return render(request, 'content/events.html',
                  {'latest_tournaments': latest_tournaments, 'latest_camps': latest_camps})


def contacts(request):
    if request.method == 'POST':
        form = sendContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = sendContact()
    return render(request, 'content/contact.html', {'form': form})

class CampsView(ListView):
    model = FootballCamp
    template_name = "content/camps.html"
    context_object_name = "camps"

class TournamentsView(ListView):
    model = Tournaments
    template_name = "content/tournaments.html"
    context_object_name = "tournaments"

class NewsView(ListView):
    model = NewsFootball
    template_name = "content/news.html"
    context_object_name = "news"

class NewsDetailView(DetailView):
    model = NewsFootball
    template_name = "content/newsDetail.html"
    context_object_name = "news"

class TournamentDetailView(DetailView):
    model = Tournaments
    template_name = "content/detailTournament.html"
    context_object_name = "tournaments"

class CampsDetailView(DetailView):
    model = FootballCamp
    template_name = "content/detailCamps.html"
    context_object_name = "camp"

def create_team(request):
    if request.method == 'POST':
        form = createApplication(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')  # Замените 'success_page' на URL страницы, куда перенаправить после успешного сохранения
    else:
        form = createApplication()

    return render(request, 'content/application.html', {'form': form})




