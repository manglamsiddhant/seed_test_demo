from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, DuelMatchSerializer, StreakSerializer , NewsArticleSerializer , DailyNewsReadSerializer, MessageSerializer
from users.models import CustomUser, Profile, DuelMatch, Streak , NewsArticle , DailyNewsRead , Message


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DuelMatchViewSet(viewsets.ModelViewSet):
    queryset = DuelMatch.objects.all()
    serializer_class = DuelMatchSerializer

class StreakViewSet(viewsets.ModelViewSet):
    queryset = Streak.objects.all()
    serializer_class = StreakSerializer

class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all().order_by('-published_at')
    serializer_class = NewsArticleSerializer

class DailyNewsReadViewSet(viewsets.ModelViewSet):
    queryset = DailyNewsRead.objects.all().order_by('-read_date')
    serializer_class = DailyNewsReadSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer


