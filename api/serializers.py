from rest_framework import serializers
from users.models import CustomUser, Profile, DuelMatch, Streak

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
