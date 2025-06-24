from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, DuelMatchViewSet, StreakViewSet , NewsArticleViewSet , DailyNewsReadViewSet, MessageViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'duels', DuelMatchViewSet)
router.register(r'streaks', StreakViewSet)
router.register(r'news-articles', NewsArticleViewSet)
router.register(r'daily-reads', DailyNewsReadViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
