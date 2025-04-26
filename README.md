
# 📚 **Bookstore Management System**

This **Bookstore Management System** is a full-stack web application built using **Django**. The system enables users to browse and purchase books, while providing admins with the ability to manage the inventory seamlessly. The application follows best practices by leveraging **Class-Based Views (CBV)** for handling requests, and it incorporates a robust **session-based** cart management system. The app does not rely on Django's default forms and admin interface, offering a custom-built admin dashboard for enhanced flexibility and control.

---

## 🌐 **Developed By**

- **Name**: Prabhat Kale
- **Roll No.**: 44
---
![Bookstore - Personal - Microsoft_ Edge 2025-04-26 15-59-31 (1)](https://github.com/user-attachments/assets/1563c1cd-f744-4ba8-9d5a-803ee2cec5dc)

## 🛠️ **Tech Stack**

### **Backend:**
- **Django**: Python-based web framework
- **SQLite**: Lightweight database (can be easily replaced with PostgreSQL or MySQL)

### **Frontend:**
- **HTML5**: Markup language for web page structure
- **CSS3**: Styling for UI/UX design
- **JavaScript**: Enhancements for interactivity

### **DevOps:**
- **Docker**: Containerization for consistent and scalable development environments
- **Docker Compose**: Simplifies multi-container setups for development
- **Jenkins**: Continuous Integration/Continuous Deployment (CI/CD) pipeline

---

## 🚀 **Key Features**

### 🔐 **User Authentication**
- **User Registration**: Manual form handling for creating new accounts
- **Login/Logout**: Secure user authentication and session management
- **Profile Management**: Users can update their profile information and manage account settings

### 🛒 **User Functionality**
- **Browse Books**: Users can explore all books available in the store
- **Book Details**: View detailed information for each book, including title, author, price, and description
- **Cart Management**: Session-based cart where users can add and remove books for purchase
- **Order Placement**: After selecting items, users can proceed to checkout for final purchase (this feature can be expanded for payments in the future)

### 🛠️ **Admin Panel**
- **Custom Admin Dashboard**: A user-friendly, customized dashboard built from scratch to manage the book inventory
- **Inventory Management**: Admins can easily add, edit, or delete books in the system
- **Book Category Management**: Organize books into categories for easier navigation
- **Order Tracking**: Track and manage orders placed by users (future enhancements)

### 🌟 **Additional Features**
- **Search & Filter**: Users can search books by title, author, or category, and filter results based on price range, ratings, etc.
- **Responsive Design**: Mobile-first design approach, ensuring a seamless user experience across devices
- **Animations**: Subtle animations for interactive elements using **Animate.css**

---

## 🐳 **Docker & Jenkins Integration**

### **Docker**
- **Dockerfile**: Defines the container image for the app, ensuring a consistent environment
- **docker-compose.yml**: Simplifies local development setup, handling dependencies like the database and web server

### **Jenkins**
- **Jenkinsfile**: Automated build and deployment pipeline, ensuring CI/CD practices are followed for smooth deployment and testing

---

## 🔧 **Setup Instructions**

To get the project up and running locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nilam-10/book-store-final
   cd bookstore
   ```

2. **Run using Docker:**
   - Build and start the containers:
     ```bash
     docker-compose up --build
     ```
   - Access the app at: [http://localhost:8000](http://localhost:8000)

---

## 🗂️ **Project Structure**

The project is organized as follows:

```
BOOK-STORE-FINAL/
├── bookstore/                   # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── books/                       # App for books and admin logic
│   ├── __init__.py
│   ├── admin.py                 # Custom admin interface logic
│   ├── apps.py
│   ├── models.py                # Database models for books
│   ├── templates/               # HTML templates for rendering views
│   ├── tests.py                 # Unit tests for app functionality
│   ├── urls.py                  # URL routing for books app
│   └── views.py                 # Views for displaying book listings, details, etc.
│
├── docker-compose.yml           # Docker Compose configuration for local dev setup
├── Dockerfile                   # Dockerfile for containerizing the app
├── Jenkinsfile                  # Jenkins CI/CD pipeline configuration
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

📸 Screenshots
Here are some screenshots showcasing the Bookstore Management System:
![alt text](<Screenshot 2025-04-25 213811.png>)
![alt text](<Screenshot 2025-04-25 214101.png>)
![alt text](<Screenshot 2025-04-25 214219.png>)
![alt text](<Screenshot 2025-04-25 213913.png>)
---

## 📄 **Future Enhancements**
- **Payment Gateway**: Integrate a payment system for users to complete their purchases online.
- **Advanced Search**: Implement advanced search and filtering options to improve user experience.
- **Review System**: Allow users to rate and review books.
- **Admin Analytics**: Add reporting features for admins, including sales statistics and inventory tracking.

---

## 🤝 **Contributing**

Feel free to fork the repository, make changes, and submit pull requests. If you find bugs or have suggestions for improvements, open an issue in the repository.

---
