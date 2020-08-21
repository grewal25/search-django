
from django.urls import path
from home.views import SearchResultsListView, HomePage


app_name = 'home'
urlpatterns = [
    path('search/', SearchResultsListView.as_view(), name = 'search_result'),
    path('', HomePage.as_view(), name = 'home'),
]
