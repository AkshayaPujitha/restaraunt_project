from django.db import models


class Pizza(models.Model):
    
    name=models.CharField(max_length=100)
    priceM=models.DecimalField(max_digits=4,decimal_places=2)
    priceL=models.DecimalField(max_digits=4,decimal_places=2)
    pImage=models.URLField()

    def get_products_by_id(ids):
        return Pizza.objects.filter(id__in =ids)
