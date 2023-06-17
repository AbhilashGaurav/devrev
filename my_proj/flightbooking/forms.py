from django import forms
from .models import Flight

class FlightBookingForm(forms.Form):
    departure_city = forms.CharField(max_length=100)
    destination_city = forms.CharField(max_length=100)
    departure_date = forms.DateField()
    num_passengers = forms.IntegerField(min_value=1, max_value=10)
    flight_choice = forms.ModelChoiceField(queryset=Flight.objects.all())
