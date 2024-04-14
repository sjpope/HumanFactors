from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=500)
    cuisine_type = models.CharField(max_length=100)
    health_rating = models.DecimalField(max_digits=2, decimal_places=1)
    price_level = models.IntegerField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class ReservationSlot(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.restaurant.name} - {self.date_time}"

