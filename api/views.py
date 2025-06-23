from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, DuelMatchSerializer, StreakSerializer
from users.models import CustomUser, Profile, DuelMatch, Streak


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


