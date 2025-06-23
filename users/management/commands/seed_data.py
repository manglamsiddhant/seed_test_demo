from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import (Profile, DuelMatch , ChatSession, Message, NewsArticle, DailyNewsRead, Streak)
from django.utils import timezone
import random

class Command(BaseCommand):
    help = "Seed the database with test users and profiles"

    def handle(self, *args, **kwargs):
        for i in range (5):
            username = f"user{i}"
            email = f"user{i}@sigmail.com"
            password = "test123"

            user, created = User.objects.get_or_create(
                username=username,
                defaults = {"email":email}
            )
            if created:
                user.set_password(password)
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Created user : {username}"))
            else:
                self.stdout.write(f"user {username} already exists")

            #check if profile already exist 
            if not hasattr(user,'profile'):
                Profile.objects.create(user=user, bio=f"This is {username}'s bio.")
                self.stdout.write(self.style.SUCCESS(f"Created profile for : {username}"))
            else:
                self.stdout.write(f"Profile for {username} already exists")
        
        # Collect all users during creation above this section
        users = User.objects.filter(username__startswith='user')

        # Create multiple DuelMatches
        for _ in range(5):
            u1, u2 = random.sample(list(users), 2)
            DuelMatch.objects.get_or_create(initiator=u1, opponent=u2, winner=random.choice([u1, u2]))
        self.stdout.write(self.style.SUCCESS("✅ Multiple DuelMatches created"))

        # Chat sessions and messages between user pairs
        for u1 in users:
            for u2 in users:
                if u1 != u2:
                    session, _ = ChatSession.objects.get_or_create(user=u1)
                    Message.objects.get_or_create(session=session, sender="user", content=f"Hello {u2.username}, what's up?")
                    Message.objects.get_or_create(session=session, sender="ai", content="Keep up with your readings, champ!")
        self.stdout.write(self.style.SUCCESS("✅ ChatSessions and Messages created"))

        # Multiple News Articles
        for i in range(3):
            article, _ = NewsArticle.objects.get_or_create(
                title=f"News Headline {i}",
                content="Breaking news content...",
                published_at=timezone.now().date()
            )
            for user in users:
                DailyNewsRead.objects.get_or_create(user=user, article=article)
                Streak.objects.get_or_create(user=user, start_date=timezone.now().date(), current_length=random.randint(1, 5))
        self.stdout.write(self.style.SUCCESS("✅ NewsArticles, Reads, and Streaks created"))
        self.stdout.write(self.style.SUCCESS("Seeding complete Good job Sid! "))



