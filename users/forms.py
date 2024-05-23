from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'street', 'colony', 'city', 'postal_code', 'external_number', 'birth_day', 'gender', 'phone']