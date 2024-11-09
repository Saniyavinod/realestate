from django.db import models

class Property(models.Model):
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    PROPERTY_TYPE_CHOICES = (
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('land', 'Land'),
        ('villa', 'Villa'),
        ('commercial', 'Commercial'),
    )
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    number_of_bedrooms = models.PositiveIntegerField()
    square_footage = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    property_image = models.ImageField(upload_to='properties/', null=True, blank=True)
    contact_details = models.CharField(max_length=255)

    def __str__(self):
        return self.address
