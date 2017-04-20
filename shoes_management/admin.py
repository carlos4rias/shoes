from django.contrib import admin

from .models import Brand, ModelBrand, Shoe, ShoeInstance, Bill, BillItem
from .models import Incoming, ItemIncoming

# Register your models here.

admin.site.register(Brand)
admin.site.register(ModelBrand)
admin.site.register(Shoe)
admin.site.register(ShoeInstance)
admin.site.register(Bill)
admin.site.register(BillItem)
admin.site.register(Incoming)
admin.site.register(ItemIncoming)
