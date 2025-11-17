from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            Activity.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()
            Leaderboard.objects.all().delete()

            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            users = [
                User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
                User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
                User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            ]

            workouts = [
                Workout.objects.create(name='Cardio', description='Cardio workout'),
                Workout.objects.create(name='Strength', description='Strength workout'),
            ]
            for w in workouts:
                w.suggested_for.set([marvel, dc])

            Activity.objects.create(user=users[0], type='run', duration=30, date=date.today())
            Activity.objects.create(user=users[1], type='cycle', duration=45, date=date.today())
            Activity.objects.create(user=users[2], type='swim', duration=25, date=date.today())
            Activity.objects.create(user=users[3], type='walk', duration=60, date=date.today())

            Leaderboard.objects.create(team=marvel, points=150)
            Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
