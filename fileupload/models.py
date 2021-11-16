from django.db import models

# Create your models here.

class Paper(models.Model):
    
    files = models.FileField(default = 1,upload_to= 'files')
    

   


