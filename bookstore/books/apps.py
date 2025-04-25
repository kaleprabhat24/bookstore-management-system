from django.apps import AppConfig

# Configuration for the Books app
# This class is used to configure the app in Django's application registry
class BooksConfig(AppConfig):
    # Define the default auto field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Name of the app
    name = 'books'
