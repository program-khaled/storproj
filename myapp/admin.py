from django.contrib import admin
from myapp.models import clothes,bag,accessory,global_brand,shoe,wristwatch,sunglas
# Register your models here.
admin.site.register(clothes)
admin.site.register(bag)
admin.site.register(accessory)
admin.site.register(global_brand)

admin.site.register(shoe)
admin.site.register(wristwatch)
admin.site.register(sunglas)