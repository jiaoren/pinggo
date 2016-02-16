from django.db import models
from django.core.files.storage import FileSystemStorage

class Furniture(models.Model):
    CATAGORY_CHOICES = (
        ('lv', 'Living Room'),
        ('kd', 'Kitchen/Dining'),
        ('of', 'Office'),
        ('br', 'Bed Room'),
        ('misc','Others'),
    )
    furnitureName = models.CharField(max_length=50)
    furnitureDescription = models.TextField(max_length=255)
    furnitureStock = models.IntegerField()
    furnitureCatagory = models.CharField(max_length=20,choices=CATAGORY_CHOICES,default='misc')
    showInMainDisplay = models.BooleanField(default=False)
    fs = FileSystemStorage(location='/var/www/Pinggo/Pinggo/static/images/')
    furnitureImage = models.FileField(storage=fs,upload_to="/var/www/Pinggo/Pinggo/static/images/")
    
    def __unicode__(self):
        return self.furnitureName    
# Create your models here.
