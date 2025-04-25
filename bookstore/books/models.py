from django.db import models

# Book model to represent a book in the bookstore
class Book(models.Model):
    # Title of the book, maximum length 255 characters
    title = models.CharField(max_length=255)
    
    # Author of the book, maximum length 255 characters
    author = models.CharField(max_length=255)
    
    # Price of the book, with a maximum of 6 digits, and 2 decimal places
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Description of the book, can be left blank
    description = models.TextField(blank=True)

    # String representation of the book, returns the title
    def __str__(self):
        return self.title
