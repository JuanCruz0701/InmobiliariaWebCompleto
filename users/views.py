from django.shortcuts import render,redirect
from django.urls import reverse
from properties.models import Property,User
from .forms import UserForm
# Create your views here.


def first_view(request):
    properties = Property.objects.all()
    colony = request.GET.get('colony')
    if colony:
        properties = properties.filter(colony__icontains=colony)

    city = request.GET.get('city')
    if city:
        properties = properties.filter(city__icontains=city)

    type = request.GET.get('type')
    if type:
        properties = properties.filter(type=type)

    ranking = request.GET.get('ranking')
    if ranking:
        properties = properties.filter(ranking=ranking)
        
    context = {
        "properties": properties
    }
    
    return render(request, "base.html", context=context)

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            properties = Property.objects.all()
            context = {
            "properties": properties,
            "form": form
        }
            return redirect(reverse('inicio'))  # redirige al usuario a la página de inicio de sesión después de registrarse
    else:
        form = UserForm()
        
    return render(request, 'user/register.html', {'form': form})