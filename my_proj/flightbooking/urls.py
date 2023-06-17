from django.urls import path
from . import views

app_name = 'flightbooking'

urlpatterns = [
    path('book-flight/', views.flight_booking, name='flight_booking'),
    path('add-flight/', views.add_flight, name='add_flight'),
    path('search-flights/', views.search_flights, name='search_flights'),
]
