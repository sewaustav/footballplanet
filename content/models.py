from django.db import models
from datetime import *

# Create your models here.
class Tournaments(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='content/static/content/images/tournaments', null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=' ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tournaments"
        verbose_name_plural = "Tournaments"

class Team(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="content/static/content/images/teams", null=True)
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    countOfPlayers = models.IntegerField()
    coach = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pnumber = models.CharField(max_length=12)
    info = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"

class SquadList(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sname = models.CharField(max_length=255)
    pos = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SquadList"
        verbose_name_plural = "SquadList"


class FootballCamp(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='content/static/content/images/camps', null=True)
    description = models.TextField()
    youtube_link = models.URLField(blank=True, null=True)
    mini_player_code = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    # Фотогалерея
    photo_gallery = models.ManyToManyField('Photo', related_name='camps', blank=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to='content/static/content/images')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Photo {self.id}"

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    pcoach = models.ImageField(upload_to='content/static/content/images/coaches', null=True )
    description = models.TextField()

    def __str__(self):
        return self.name

class Training(models.Model):
    camp = models.ForeignKey(FootballCamp, on_delete=models.CASCADE, related_name='trainings')
    photo = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='training_photos', null=True  )
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='related_trainings')
    training_description = models.TextField()

    def __str__(self):
        return f"{self.trainer} - {self.camp.name}"



class Match(models.Model):
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    team_home = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    team_away = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    result_home = models.IntegerField(null=True, blank=True)
    result_away = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.team_home} vs. {self.team_away} - {self.date_time}"

class Standing(models.Model):
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    group = models.CharField(max_length=2)
    points = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team} - Points: {self.points}"


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    topic = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class NewsFootball(models.Model):
    name = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="content/static/content/images/news")
    time_of_publication = models.DateTimeField(null=True)
    text = models.TextField()

    def __str__(self):
        return self.name





