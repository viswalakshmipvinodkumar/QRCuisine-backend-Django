from django.db import models
from authentication.models import Restaurant, Chef
from menu.models import MenuItem

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Being Prepared', 'Being Prepared'),
        ('Ready to Serve', 'Ready to Serve'),
        ('Delivered', 'Delivered')
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    menu_items = models.ManyToManyField(MenuItem)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Table {self.table_number} - {self.status}"
