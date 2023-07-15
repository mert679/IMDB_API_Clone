from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class MovieListPaginaion(LimitOffsetPagination):
    default_limit = 5
   
class MovieReviewListPaginaion(PageNumberPagination):
    page_size = 10
