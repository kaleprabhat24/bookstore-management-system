from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView, BookListView, BookDetailView,
    AddToCartView, CartView, RemoveFromCartView, AdminPanelView,
    AdminBookCreateView, AdminBookEditView, AdminBookDeleteView
)

# URL routing for the bookstore application
urlpatterns = [
    # User Authentication URLs
    # Register a new user
    path('register/', RegisterView.as_view(), name='register'),
    
    # User login page
    path('login/', LoginView.as_view(), name='login'),
    
    # User logout page
    path('logout/', LogoutView.as_view(), name='logout'),

    # User-facing Pages (Bookstore Pages)
    # Home page: Display the list of all books
    path('', BookListView.as_view(), name='book_list'),
    
    # Book detail page: Display details of a specific book
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),

    # Cart Pages
    # Add a specific book to the cart
    path('cart/add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    
    # View the user's shopping cart
    path('cart/', CartView.as_view(), name='cart'),
    
    # Remove a specific item from the cart
    path('cart/remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),

    # Admin Panel for Book Management (Only accessible by superusers)
    # Admin panel: Manage books and perform actions like sorting, viewing, etc.
    path('admin/', AdminPanelView.as_view(), name='admin_panel'),
    
    # Admin action: Create a new book entry
    path('admin/book/create/', AdminBookCreateView.as_view(), name='admin_book_create'),
    
    # Admin action: Edit an existing book
    path('admin/book/edit/<int:pk>/', AdminBookEditView.as_view(), name='admin_book_edit'),
    
    # Admin action: Delete a book entry
    path('admin/book/delete/<int:pk>/', AdminBookDeleteView.as_view(), name='admin_book_delete'),
]
