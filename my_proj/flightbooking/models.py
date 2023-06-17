from django.db import models

class Flight(models.Model):
    flight_name = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)

    def __str__(self):
        return self.flight_name
