from django.db import models


# Create your models here.
class AddBook(models.Model):
    book_name = models.CharField(max_length=255)
    book_image= models.ImageField(default='fallback.png', blank=True)
    book_price= models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.book_name
    
class EditBook(models.Model):
    book_name = models.CharField(max_length=255)
    book_image= models.ImageField(default='fallback.png', blank=True)
    book_price= models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.book_name