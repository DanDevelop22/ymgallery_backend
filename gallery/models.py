from django.db import models

class Paint(models.Model):
    """Modelo con los datos de cada cuadro a tokenizar"""   
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='paintings/%Y/%m/%d')
    author = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    description = models.TextField(blank=True,null=True)
    #user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='paint', unique=False, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Cuadro"
        verbose_name_plural = "Cuadros"
