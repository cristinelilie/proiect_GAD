from django.db import models
from django.contrib.auth.models import User

# class myModel(models.Model):
#     class Meta:
#         abstract = True
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Products(models.Model):
    class Meta:
        db_table = 'products'
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.CharField(max_length=100)
    description = models.TextField(max_length=255, null=True, blank=True)
    cumparat = models.BooleanField(default=False)

    def __str__(self):
        return self.product + "-->" + str(self.cumparat)

    class Meta:
        ordering = ['product']


