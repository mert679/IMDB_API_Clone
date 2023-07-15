from watchlist_app.models import WatchList, MovieReview, MoviePlatform
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle, UserRateThrottle
from rest_framework.filters import SearchFilter, OrderingFilter

from .permission import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from .serializers import WatchListSerializer, MoviePlatformSerializer, MovieReviewSerializer
from .pagination import MovieListPaginaion, MovieReviewListPaginaion
from .throttling import ReviewCreateThrottle, ReviewListThrottle, WatchListThrottle



class WatchListGV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = MovieListPaginaion
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields=['title']
    throttle_classes = [WatchListThrottle, AnonRateThrottle]

class WatchListDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated]

class MoviePlatformListGV(generics.ListCreateAPIView):
    queryset = MoviePlatform.objects.all()
    serializer_class = MoviePlatformSerializer
    permission_classes = [IsAdminOrReadOnly]


class MoviePlatformDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, name):
        try:
            platform = MoviePlatform.objects.get(name=name)
        except MoviePlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializedData = MoviePlatformSerializer(platform).data
        return Response(serializedData)
    
    def put(self,request,name):
        platform = MoviePlatform.objects.get(name=name)
        serializer = MoviePlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,name):
        platform = MoviePlatform.objects.get(name=name)
        platform.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MovieReviewDetailGV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    # with this code filtering movie pk.
    def get_queryset(self):
        pk = self.kwargs['pk']
        return MovieReview.objects.filter(watchlist=pk)
    
class MovieReviewListGV(generics.ListAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = MovieReviewListPaginaion
    filter_backends = [OrderingFilter]
    ordering_fields = ["created"]
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]

class MoviewReviewCreateGV(generics.CreateAPIView):
    serializer_class = MovieReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]
    
    def get_queryset(self):
        return MovieReview.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        watchlist = WatchList.objects.get(id=pk)
        review_user = self.request.user
        review_queryset = MovieReview.objects.filter(review_user = review_user, watchlist=watchlist)

        if review_queryset.exists():
            raise ValidationError('You have already reviewed the selected movie.')
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (
                watchlist.avg_rating + serializer.validated_data['rating'])/2

        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, review_user=review_user)


class UserReview(generics.ListAPIView):
    serializer_class = MovieReviewSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = MovieReview.objects.filter(review_user__username=username)
        return queryset
        