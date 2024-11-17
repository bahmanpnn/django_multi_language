from django.db import models


class Product(models.Model):
    title=models.CharField(max_length=127,null=True,verbose_name='product title')
    price=models.PositiveIntegerField(default=0,verbose_name='product price')

    def __str__(self):
        return self.title

