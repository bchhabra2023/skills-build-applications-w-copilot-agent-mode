from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        app_models.User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        users = [
            app_models.User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            app_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            app_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            app_models.User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        activities = [
            app_models.Activity.objects.create(user=users[0], type='Running', duration=30),
            app_models.Activity.objects.create(user=users[1], type='Cycling', duration=45),
            app_models.Activity.objects.create(user=users[2], type='Swimming', duration=60),
            app_models.Activity.objects.create(user=users[3], type='Yoga', duration=50),
        ]

        # Create Workouts
        workouts = [
            app_models.Workout.objects.create(name='Morning Cardio', description='Cardio workout for all'),
            app_models.Workout.objects.create(name='Strength Training', description='Strength workout for heroes'),
        ]

        # Create Leaderboard
        app_models.Leaderboard.objects.create(user=users[0], score=100)
        app_models.Leaderboard.objects.create(user=users[1], score=90)
        app_models.Leaderboard.objects.create(user=users[2], score=95)
        app_models.Leaderboard.objects.create(user=users[3], score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
