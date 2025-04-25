from django.contrib import admin
from .models import Book

# Registering the Book model to display it in the Django admin interface
# This allows the admin user to view, edit, and manage Book objects from the admin panel
admin.site.register(Book)
