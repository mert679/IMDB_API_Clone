from django.contrib import admin
from .models import WatchList, MoviePlatform, MovieReview
# Register your models here.
admin.site.register(WatchList)
admin.site.register(MoviePlatform)
admin.site.register(MovieReview)