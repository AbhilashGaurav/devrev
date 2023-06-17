from django.shortcuts import render, redirect
from .forms import FlightBookingForm
from .models import Flight

from django.shortcuts import render
from .models import Flight

def flight_booking(request):
    if request.method == 'POST':
        # Retrieve the form data
        flight_name = request.POST['flight_name']
        departure_date = request.POST['departure_date']
        departure_time = request.POST['departure_time']
        airport_name = request.POST['airport_name']
        
        # Save the booking details or perform other operations
        
        # Render the success page
        return render(request, 'flightbooking/success.html')

    else:
        # Retrieve the available flights
        available_flights = Flight.objects.all()
        
        # Render the flight booking form with available flights data
        return render(request, 'flightbooking/flight_booking.html', {'flights': available_flights})


def add_flight(request):
    if request.method == 'POST':
        # Create a new flight
        flight_name = request.POST['flight_name']
        departure_date = request.POST['departure_date']
        departure_time = request.POST['departure_time']
        departure_city = request.POST['departure_city']
        destination_city = request.POST['destination_city']
        
        Flight.objects.create(
            flight_name=flight_name,
            departure_date=departure_date,
            departure_time=departure_time,
            departure_city=departure_city,
            destination_city=destination_city
        )
        
        # Redirect to the flight booking page
        return redirect('flightbooking:flight_booking')
    
    return render(request, 'flightbooking/add_flight.html')

def search_flights(request):
    departure_date = request.GET.get('departure_date')
    departure_time = request.GET.get('departure_time')

    if departure_date and departure_time:
        flights = Flight.objects.filter(departure_date=departure_date, departure_time__gte=departure_time)
    else:
        flights = []  # or handle the case when the parameters are missing

    return render(request, 'flightbooking/flight_search.html', {'flights': flights})
