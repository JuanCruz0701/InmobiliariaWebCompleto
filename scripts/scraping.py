from lxml import etree
import requests
from io import StringIO
import re
from properties.models import Property

def run():
    response = requests.get("https://mexico.inmobiliarie.com/inmuebles-en-venta-y-renta/terreno-en-lomas-del-centinela-cerca-de-universidades/")
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(str(response.content)), parser)
    
    description = tree.xpath('//div[@class="directorist-listing-details__text"]//span/text()')[3]
    ubicacion = tree.xpath('//a[@target="google_map"]/text()')[0]
    precio = tree.xpath('//div[@class="directorist-info-item directorist-pricing-meta directorist-info-item-price"]//span/text()')
    tipo = tree.xpath('//span/a/text()')[6]
    alto = tree.xpath('//div[@class="directorist-single-info__value"]/text()')[1]
    ancho = tree.xpath('//div[@class="directorist-single-info__value"]/text()')[1]
    
    calle = re.search('Roble', ubicacion)
    colonia = re.search('Lomas del Centinela', ubicacion)
    ciudad = re.search('Jalisco', ubicacion)
    postal = re.search('45204', ubicacion)
    
    print(f'descripcion:{description}') 

    if calle and colonia and ciudad and postal:
        print(f'calle: {calle.group()}')
        print(f'colonia: {colonia.group()}')
        print(f'ciudad: {ciudad.group()}')
        print(f'codigo postal: {postal.group()}')
    print(f'precio:{precio}') 

    # Limpieza del precio
    if precio:
        precio_limpio = precio[0].replace('$', '').replace(',', '')
        precio_float = float(precio_limpio)
    else:
        precio_float = None

    propiedad = Property()
    propiedad.description = description
    propiedad.street = calle.group() if calle else None
    propiedad.colony = colonia.group() if colonia else None
    propiedad.city = ciudad.group() if ciudad else None
    propiedad.postal_code = postal.group() if postal else None
    propiedad.price = precio_float
    propiedad.type = tipo
    propiedad.wide = float(ancho)
    propiedad.long = float(alto)
    propiedad.save()