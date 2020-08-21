from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.cat_name
    
    class Meta:
        verbose_name_plural = 'categories'

class Book(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name

