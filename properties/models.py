from django.db import models
from users.models import User
import os.path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Property(models.Model):
    HOUSE = "house"
    DEPARTMENT = "deparment"
    LAND = "land"
    TYPE_PROPERTY = (
        (HOUSE, "Casa"),
        (DEPARTMENT, "Departamento"),
        (LAND, "Terreno"),
    )
    description = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    colony = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)
    external_number = models.CharField(max_length=5, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=100, choices=TYPE_PROPERTY, blank=True, null=True)
    wide = models.FloatField(default=0)
    long = models.FloatField(default=0)
    ranking = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="property_user",
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(upload_to='thumbs', editable=False, blank=True, null=True)
    def __str__(self):
        return self.description
    def make_thumbnail(self):
        image = Image.open(self.image)
        thumbnail_size = 75, 75
        image.thumbnail(thumbnail_size)
        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + '_thumb' + thumb_extension
        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)
       
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        return True
class PropertyBuy(models.Model):
    buyer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="propertybuy_user",
        blank=True,
        null=True
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.PROTECT,
        related_name="propertybuy_user",
        blank=True,
        null=True
    )
    def __str__(self):
        return self.property.description
