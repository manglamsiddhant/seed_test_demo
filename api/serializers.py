from rest_framework import serializers
from users.models import CustomUser, Profile, DuelMatch, Streak , NewsArticle , DailyNewsRead , Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'location']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class DuelMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuelMatch
        fields = '__all__'

class StreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streak
        fields = '__all__'

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = '__all__'

class DailyNewsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyNewsRead
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
