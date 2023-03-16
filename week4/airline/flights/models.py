from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

# 1. As we discussed, passengers have a Many to Many relationship with 
# flights, which we describe in Django using the ManyToManyField.

# 2.The first argument in this field is the class of objects that this 
# one is related to.

# 3. We have provided the argument blank=True which means a 
# passenger can have no flights

# 4.We have added a related_name that serves the same purpose 
# as it did earlier: it will allow us to find all passengers on 
# a given flight.

    def __str__(self):
        return f"{self.first} {self.last}"