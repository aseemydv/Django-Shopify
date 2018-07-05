from django.db import models

class add_product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.title
