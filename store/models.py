from django.db import models

# Create your models here.
class Shoe(models.Model):

    BRANDS= (
        ('NIKE','NIKE'),
        ('ADIDAS','ADIDAS'),
        ('PUMA','PUMA'),
    )

    name = models.CharField(max_length = 150)
    brand = models.CharField(max_length = 150,choices =BRANDS,default='NIKE')
 
    def __str__(self):
        return self.name