import qrcode
from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO

class MenuItem(models.Model):
    restaurant = models.ForeignKey("authentication.Restaurant", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class QRCode(models.Model):
    restaurant = models.OneToOneField("authentication.Restaurant", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qrcodes/')

    def save(self, *args, **kwargs):
        qr_data = f"https://qrcuisine.com/menu/{self.restaurant.id}"
        qr = qrcode.make(qr_data)
        qr_io = BytesIO()
        qr.save(qr_io, format='PNG')
        self.qr_code.save(f"{self.restaurant.id}_qrcode.png", ContentFile(qr_io.getvalue()), save=False)
        super().save(*args, **kwargs)
