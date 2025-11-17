from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, date='2025-11-17')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 100)

    def test_activity_type(self):
        self.assertEqual(self.activity.type, 'run')
