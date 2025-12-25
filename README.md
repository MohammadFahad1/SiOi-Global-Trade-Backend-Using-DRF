# 🛒 Django REST eCommerce API

A fully-featured **eCommerce REST API** built with **Django Rest Framework (DRF)**.  
This project provides scalable, secure, and well-documented APIs for managing an online store, including authentication, product management, cart handling, and order processing.

---

### ☯️ Project Live Link

[https://sioi-global-trade-backend-using-drf.vercel.app/](https://sioi-global-trade-backend-using-drf.vercel.app/)

## 🚀 Features

### 🔐 Authentication & Authorization

- JWT Authentication using **Djoser** + **SimpleJWT**
- Role-based access (Admin & User)
- Secure login, logout, token refresh

### 📦 Core Modules

- Categories
- Brands
- Products
- Product Reviews
- Carts
- Orders

### 📄 API Documentation

- Interactive API documentation using **Swagger (drf_yasg)**

### 🗄️ Database

- **PostgreSQL** for reliability and performance

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** Djoser, SimpleJWT
- **Database:** PostgreSQL
- **API Docs:** drf_yasg (Swagger)
- **Language:** Python 3.x

---

## 📂 Project Structure (Simplified)

```

project_root/
├── api/
├── order/
├── product/
├── sioi_global_trade/
├── users/
├── manage.py
└── requirements.txt

```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git https://github.com/MohammadFahad1/SiOi-Global-Trade-Backend-Using-DRF.git
cd SiOi-Global-Trade-Backend-Using-DRF
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac/Bash
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file and configure:

```env
# Django Secret Key
SECRET_KEY=your_project_secret_key

# Database Configuration
user=your_db_user
password=your_db_password
host=your_db_host
port=5432 (correct if the is not default)
dbname=postgres (correct if not default)

# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME=enter_your_cloud_name
CLOUDINARY_API_KEY=enter_your_api_key
CLOUDINARY_API_SECRET=enter_your_api_secret
CLOUDINARY_URL=enter_your_cloudinary_url

# Email configuration
EMAIL_HOST=your_email_host
EMAIL_USE_TLS=True (Change to False if not using TLS)
EMAIL_PORT=587 (Default port for TLS)
EMAIL_HOST_USER=your_email_address
EMAIL_HOST_PASSWORD=your_email_password
```

### 5️⃣ Run Migrations

```bash
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run Development Server

```bash
python manage.py runserver
```

---

## 🔑 Demo Credentials (For Testing Only)

> ⚠️ **These credentials are for development/testing purposes only**

### 👑 Admin User

```
Email: admin@sioi.com
Password: admin@123
```

### 👤 Normal User

```
Email: user@sioi.com
Password: user@123
```

---

## 🔐 Authentication Endpoints

| Action        | Endpoint             |
| ------------- | -------------------- |
| Login         | `/auth/jwt/create/`  |
| Refresh Token | `/auth/jwt/refresh/` |
| Register      | `/auth/users/`       |

---

## 📦 API Modules Overview

### 🗂️ Categories

- Create, update, delete (Admin)
- List & retrieve (Public)

### 🏷️ Brands

- CRUD operations (Admin)
- Read access (Public)

### 📦 Products

- CRUD operations
- Product filtering & search
- Category & brand association

### ⭐ Reviews

- Authenticated users can add reviews
- Review moderation support

### 🛒 Cart

- Add/remove products
- Quantity update
- Authenticated user carts

### 📑 Orders

- Place orders
- Order history
- Order status tracking

---

## 📘 API Documentation (Swagger)

Once the server is running, access Swagger UI at:

```
http://127.0.0.1:8000/swagger/
```

or

```
http://127.0.0.1:8000/redoc/
```

---

## 🔒 Security Notes

- JWT tokens are required for protected endpoints
- Admin-only endpoints are role-restricted
- Passwords are hashed using Django’s default security

---

## 📌 Future Improvements

- Payment gateway integration
- Product wishlist
- Order invoice generation
- Email notifications
- Caching with Redis

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the project and submit a pull request.

---

## 📄 License

[MIT License](LICENSE)
Copyright (c) 2025 Md. Fahad Monshi

---

## 👨‍💻 Author

Developed by [**Md. Fahad Monshi**](https://fahadbd.com)
Software Developer (Full Stack) | Django & REST APIs
