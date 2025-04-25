from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Book

# Register view for user registration
class RegisterView(View):
    def get(self, request):
        # Renders the registration form
        return render(request, 'register.html')

    def post(self, request):
        # Handles user registration logic
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate if username and password are provided
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        # Create the new user
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')


# Login view for user authentication
class LoginView(View):
    def get(self, request):
        # Renders the login form
        return render(request, 'login.html')

    def post(self, request):
        # Handles login logic
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')

        messages.error(request, 'Invalid username or password.')
        return redirect('login')


# Logout view to log the user out
class LogoutView(View):
    def get(self, request):
        # Logs the user out and redirects to login
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect('login')


# Display list of books for all users
class BookListView(View):
    def get(self, request):
        # Fetch all books and render the book list
        books = Book.objects.all()
        return render(request, 'book_list.html', {'books': books})


# Display details of a specific book
class BookDetailView(View):
    def get(self, request, pk):
        # Fetch the book using primary key and render the book details
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'book_detail.html', {'book': book})


# Add a book to the cart
class AddToCartView(View):
    def post(self, request, pk):
        # Add the selected book to the shopping cart
        book = get_object_or_404(Book, pk=pk)
        cart = request.session.get('cart', {})

        # Update the quantity of the book in the cart
        cart[str(book.id)] = cart.get(str(book.id), 0) + 1
        request.session['cart'] = cart
        messages.success(request, f'{book.title} added to cart.')
        return redirect('book_list')


# View the cart contents
class CartView(View):
    def get(self, request):
        # Display cart contents and calculate total price
        cart = request.session.get('cart', {})
        books = Book.objects.filter(id__in=cart.keys())
        cart_items = [{'book': book, 'quantity': cart[str(book.id)]} for book in books]
        total_price = sum(item['book'].price * item['quantity'] for item in cart_items)
        return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


# Remove an item from the cart
class RemoveFromCartView(View):
    def get(self, request, item_id):
        # Remove the item from the shopping cart
        cart = request.session.get('cart', {})
        if str(item_id) in cart:
            del cart[str(item_id)]
            request.session['cart'] = cart
            messages.success(request, 'Item removed from cart.')
        return redirect('cart')


# Admin panel to manage books
class AdminPanelView(View):
    def get(self, request):
        # Ensure the user is an admin before allowing access
        if not request.user.is_superuser:
            messages.error(request, 'You are not authorized to access the admin panel.')
            return HttpResponse('Unauthorized', status=401)

        # Sorting logic
        sort_by = request.GET.get('sort', 'title')
        sort_order = request.GET.get('order', 'asc')
        order_prefix = '-' if sort_order == 'desc' else ''
        if sort_by not in ['title', 'author', 'price']:
            sort_by = 'title'

        books = Book.objects.all().order_by(f'{order_prefix}{sort_by}')

        # Pagination setup
        paginator = Paginator(books, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'admin_panel.html', {
            'books': page_obj,
            'page_obj': page_obj,
            'sort_by': sort_by,
            'sort_order': sort_order,
        })


# Admin view to create a new book
class AdminBookCreateView(View):
    def get(self, request):
        # Ensure the user is an admin before rendering the form
        if not request.user.is_superuser:
            messages.error(request, 'You are not authorized to access this page.')
            return HttpResponse('Unauthorized', status=401)
        return render(request, 'admin_book_form.html')

    def post(self, request):
        # Ensure the user is an admin before proceeding
        if not request.user.is_superuser:
            messages.error(request, 'You are not authorized to access this page.')
            return HttpResponse('Unauthorized', status=401)

        # Get the form data
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        description = request.POST.get('description', '')

        # Validate form inputs
        errors = []
        if not title:
            errors.append('Title is required.')
        if not author:
            errors.append('Author is required.')
        if not price:
            errors.append('Price is required.')
        try:
            price = float(price)
            if price < 0:
                errors.append('Price cannot be negative.')
        except (ValueError, TypeError):
            errors.append('Price must be a valid number.')

        # If there are errors, display them and re-render the form
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'admin_book_form.html', {
                'title': title,
                'author': author,
                'price': price,
                'description': description
            })

        # Create the new book
        book = Book.objects.create(
            title=title,
            author=author,
            price=price,
            description=description
        )
        messages.success(request, f'Book "{book.title}" created successfully.')
        return redirect('admin_panel')


# Admin view to edit an existing book
class AdminBookEditView(View):
    def get(self, request, pk):
        # Ensure the user is an admin before accessing the page
        if not request.user.is_superuser:
            messages.error(request, 'You are not authorized to access this page.')
            return HttpResponse('Unauthorized', status=401)
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'admin_book_form.html', {'book': book})

    def post(self, request, pk):
        # Ensure the user is an admin before proceeding
        if not request.user.is_superuser:
            messages.error(request, 'You are not authorized to access this page.')
            return HttpResponse('Unauthorized', status=401)

        # Get the form data and validate it
        book = get_object_or_404(Book, pk=pk)
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        description = request.POST.get('description', '')

        errors = []
        if not title:
            errors.append('Title is required.')
        if not author:
            errors.append('Author is required.')
        if not price:
            errors.append('Price is required.')
        try:
            price = float(price)
            if price < 0:
                errors.append('Price cannot be negative.')
        except (ValueError, TypeError):
            errors.append('Price must be a valid number.')

        # If there are errors, display them and re-render the form
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'admin_book_form.html', {
                'book': book,
                'title': title,
                'author': author,
                'price': price,
                'description': description
            })

        # Save the updated book details
        book.title = title
        book.author = author
        book.price = price
        book.description = description
        book.save()
        messages.success(request, f'Book "{book.title}" updated successfully.')
        return redirect('admin_panel')


# Admin view to delete a book
class AdminBookDeleteView(View):
    def post(self, request, pk):
        # Ensure the user is an admin before deleting the book
        if not request.user.is_superuser:
            messages.error(request, 'You are not authorized to access this page.')
            return HttpResponse('Unauthorized', status=401)

        # Delete the book and show a success message
        book = get_object_or_404(Book, pk=pk)
        title = book.title
        book.delete()
        messages.success(request, f'Book "{title}" deleted successfully.')
        return redirect('admin_panel')
