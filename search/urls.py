from django.urls import path

from search.views import SearchCompanies, SearchUsers

urlpatterns = [
    path('user/<str:query>/', SearchUsers.as_view()),
    path('company/<str:query>/', SearchCompanies.as_view()),
]