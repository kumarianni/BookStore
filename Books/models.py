from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    stock=models.PositiveIntegerField()
    cover_image=models.URLField(blank=True)


    def __str__(self):
        return self.title
    