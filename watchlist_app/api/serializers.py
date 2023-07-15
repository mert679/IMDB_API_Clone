from watchlist_app.models import WatchList, MovieReview, MoviePlatform
from rest_framework import serializers

class MovieReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    watchlist = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = MovieReview
        fields  = "__all__"
    
class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.CharField( source ="movie_platform.name")
    class Meta:
        model = WatchList
        fields  = "__all__"

class MoviePlatformSerializer(serializers.ModelSerializer):
    WatchList = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = MoviePlatform
        fields  = "__all__"