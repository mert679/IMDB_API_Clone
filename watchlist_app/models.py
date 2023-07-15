from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class MoviePlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active  = models.BooleanField()
    number_rating = models.IntegerField(default=0)
    avg_rating = models.FloatField(default=0)
    movie_platform = models.ForeignKey(MoviePlatform, on_delete=models.CASCADE,related_name="watchlist")

    def __str__(self):
        return self.title

class MovieReview(models.Model):
    review_user = models.ForeignKey(User ,on_delete=models.CASCADE)
    watchlist = models.ForeignKey(WatchList, related_name='reviews' ,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) # Rating should be between (1-5)
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.review_user} {self.rating}"