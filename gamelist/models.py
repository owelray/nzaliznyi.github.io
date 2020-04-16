from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class GameReview(models.Model):
    game_title = models.CharField(max_length=128)
    review = models.CharField(max_length=450)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=10, default=0)
    likenumber = models.IntegerField(default=0)
    likedone = models.ManyToManyField(User, related_name='users_likes')
    date = models.DateTimeField(auto_now_add=True)