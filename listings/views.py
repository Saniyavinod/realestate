from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .forms import PropertyForm
from .models import Property

# Add Property
class ListingsCreateView(View):
    form_class = PropertyForm
    template_name = 'property_add.html'

    def get(self, request, *args, **kwargs):
        form_instance = self.form_class()
        return render(request, self.template_name, {'form': form_instance})

    def post(self, request, *args, **kwargs):
        form_instance = self.form_class(request.POST, request.FILES)
        
        if form_instance.is_valid():
            form_instance.save()
            return redirect('property_list')  # Redirect to 'property_list'

        return render(request, self.template_name, {'form': form_instance})

# Property List View
class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'  # Template to display properties
    context_object_name = 'properties'

# Edit Property
class PropertyEditView(View):
    form_class = PropertyForm
    template_name = 'property_edit.html'

    def get(self, request, pk, *args, **kwargs):
        property_instance = get_object_or_404(Property, pk=pk)
        form_instance = self.form_class(instance=property_instance)
        return render(request, self.template_name, {'form': form_instance})

    def post(self, request, pk, *args, **kwargs):
        property_instance = get_object_or_404(Property, pk=pk)
        form_instance = self.form_class(request.POST, request.FILES, instance=property_instance)

        if form_instance.is_valid():
            form_instance.save()
            return redirect('property_list')  # Redirect to 'property_list'

        return render(request, self.template_name, {'form': form_instance})

# Delete Property
class PropertyDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        property_instance = get_object_or_404(Property, pk=pk)
        return render(request, 'confirmation_delete.html', {'property': property_instance})

    def post(self, request, pk, *args, **kwargs):
        property_instance = get_object_or_404(Property, pk=pk)
        property_instance.delete()
        return redirect('property_list')  # Redirect to 'property_list'
