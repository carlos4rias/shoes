from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ModelBrand(models.Model):
    model = models.CharField(max_length=50)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{brand}  {name}".format(name=self.model, brand=self.brand.name)

class Shoe(models.Model):
    modelBrand = models.OneToOneField('ModelBrand', on_delete=models.SET_NULL, null=True)

    GENRE = (
        ('h', 'Hombre'),
        ('m', 'Mujer'),
        ('u', 'Unisex'),
    )
    genre = models.CharField(max_length=1, choices=GENRE, blank=True, default='h')

    STYLE = (
        ('de', 'deportivo'),
        ('fo', 'formal'),
    )
    style = models.CharField(max_length=2, choices=STYLE, blank=True, default='de')


    def __str__(self):
        return self.modelBrand.model

    def get_absolute_url(self):
        return reverse('shoe-detail', args=[str(self.id)])

class ShoeInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    shoe = models.ForeignKey('Shoe', on_delete=models.SET_NULL, null=True)

    SIZES = (
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
    )
    size = models.CharField(max_length=2, choices=SIZES, blank=True, default='27')
    price = models.FloatField(default=0.0)

    STATE = (
        ('on', 'stacked'),
        ('of', 'vendido'),
        ('de', 'devolucion')
    )
    state = models.CharField(max_length=2, choices=STATE, blank=True, default='on')

    def __str__(self):
        return "{id} : {shoe}".format(id=self.id, shoe=self.shoe.modelBrand.model)

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.CharField(max_length=20, blank=False)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sold_date = models.DateField()

    def __str__(self):
        return "{id} : {seller} - {buyer}".format(id=self.id, seller=self.seller.username, buyer=self.sold_date)

class BillItem(models.Model):
    bill = models.ForeignKey('Bill', on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey('ShoeInstance', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.bill.seller.username

class Incoming(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField()

class ItemIncoming(models.Model):
    incoming = models.ForeignKey('Incoming', on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey('ShoeInstance', on_delete=models.SET_NULL, null=True)
