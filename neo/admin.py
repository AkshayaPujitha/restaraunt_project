from django.contrib import admin
from .models import Pizza
# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display=('name','priceM','priceL')
admin.site.register(Pizza,PizzaAdmin)