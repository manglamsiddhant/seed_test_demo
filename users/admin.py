from django.contrib import admin
from .models import Profile , DuelMatch , ChatSession , Message, NewsArticle , DailyNewsRead, Streak

admin.site.register(Profile)
admin.site.register(DuelMatch)
admin.site.register(ChatSession)
admin.site.register(Message)
admin.site.register(NewsArticle)
admin.site.register(DailyNewsRead)
admin.site.register(Streak) 
