from django.contrib import admin
from properties.models import Property, PropertyBuy
# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "street",
        "city",
        "owner",
        "thumbnail",
    )


@admin.register(PropertyBuy)
class Propertybuyadmin(admin.ModelAdmin):
    list_display = (
        "id",
        "buyer",
        "property"
    )
