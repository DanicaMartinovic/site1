from django.db import models


CATEGORY_CHOICES=(
    ('VO', 'Voce'),
    ('PO', 'Povrce'),
)
# Create your models here.
class Proizvod(models.Model):
    naziv = models.CharField(max_length=100)
    cena = models.FloatField()
    kategorija = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    opis= models.TextField()
    product_image = models.ImageField(upload_to='image')
    
    def __str__(self):
        return self.naziv
    
