from django.forms import ModelForm
from .models import Property,PropertyBuy


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = "__all__"

class PropertyBuyForm(ModelForm):
    class Meta:
        model = PropertyBuy
        fields = "__all__"




    
