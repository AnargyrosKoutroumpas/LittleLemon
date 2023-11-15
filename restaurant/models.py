from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
    class Meta:
        verbose_name='Booking'
        verbose_name_plural='Bookings'
        ordering=['booking_date']

    def __str__(self):
        return f'{self.name} x{self.no_of_guests} @{self.booking_date}'

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    class Meta:
        verbose_name='Menu'
        verbose_name_plural='Menu'
        ordering=['title']

    def __str__(self):
        return self.title