from django.shortcuts import render, get_object_or_404, redirect
from .forms import PropertyForm, PropertyBuyForm
from .models import Property, PropertyBuy
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
import logging
from django.contrib.auth.decorators import login_required

def PropertyView(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        properties = Property.objects.all()
        context = {
            "properties": properties,
            "form": form
        }
        return render(request, "properties/property_list.html", context=context)
    else:
        form = PropertyForm()
        context = {
            "form": form
        }
        return render(request, "properties/property_form.html", context=context)

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_info.html'
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PropertyBuyForm()
        return context

logger = logging.getLogger(__name__)
@login_required
def buy_property(request, property_id):
    logger.info('Accediendo a la vista buy_property con property_id: %s', property_id)
    property = get_object_or_404(Property, id=property_id)
    if request.method == "POST":
        form = PropertyBuyForm(request.POST)
        if form.is_valid():
            property_buy = form.save(commit=False)
            property_buy.buyer = request.user
            property_buy.property = property
            property_buy.save()
            return redirect('property_detail', pk=property.id)
    else:
        form = PropertyBuyForm()

    return render(request, 'properties/buy_property.html', {'form': form, 'property': property})

    
    
   
    