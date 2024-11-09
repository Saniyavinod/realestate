from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'price', 'property_type', 'number_of_bedrooms', 'square_footage', 'location', 'property_image', 'contact_details']
