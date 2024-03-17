from django.db import models
from django.contrib.auth.models import User
class MatatuRoute(models.Model):
    route_name = models.CharField(max_length=50)
    starting_point = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return (f'{self.route_name} - {self.starting_point} to {self.destination}')
    
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(MatatuRoute, on_delete=models.CASCADE)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    seat_number = models.IntegerField()
    
    def __str__(self):
        return (f'{self.username} - {self.route_name} - Seat {self.seat_number}')
    
