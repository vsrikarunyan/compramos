# shopping_lists/api/pagination.py

from rest_framework.pagination import PageNumberPagination

class LargerResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

