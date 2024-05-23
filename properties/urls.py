from django.urls import path, include
from .views import PropertyView

urlpatterns = [
    path('form/', PropertyView, name="form-property"),
    
    
]