from django.urls import path
from .views import WatchListGV, WatchListDetailGV, MoviePlatformListGV, MoviePlatformDetailAV, MovieReviewListGV, MovieReviewDetailGV, MoviewReviewCreateGV, UserReview

urlpatterns = [
    path("list/", WatchListGV.as_view(), name="movie_list"),
    path("list/<int:pk>/", WatchListDetailGV.as_view(), name="movie_detail"),
    path("platform/", MoviePlatformListGV.as_view(), name="platform_list"),
    path("platform/<str:name>/", MoviePlatformDetailAV.as_view(), name="platform_detail"),
    path("reviews/", MovieReviewListGV.as_view(), name="review_list"),
    path("<int:pk>/reviews/", MovieReviewDetailGV.as_view(), name="review_detail"),
    path("<int:pk>/reviews/create/", MoviewReviewCreateGV.as_view(), name="review_create"),
    path("user-reviews/", UserReview.as_view(), name="user_review_detail"),
]