from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, DuelMatchViewSet, StreakViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'duels', DuelMatchViewSet)
router.register(r'streaks', StreakViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
