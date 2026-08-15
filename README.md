# College ERP

> A Django REST API for managing students, faculty, courses, enrollments, attendance, examinations, grades, timetables and fees.

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-REST%20API-red)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)](https://www.postgresql.org/)
[![JWT](https://img.shields.io/badge/Auth-JWT-orange)](https://django-rest-framework-simplejwt.readthedocs.io/)

---

## 📌 Overview

College ERP is a backend application designed to manage the core academic and administrative operations of a college.

The project is built with **Django**, **Django REST Framework**, and **PostgreSQL**, and exposes a RESTful API that can later be consumed by a React or other frontend application.

### Main goals

* Manage students and faculty
* Organize departments and courses
* Manage student enrollments
* Track attendance
* Create academic timetables
* Manage examinations and grades
* Manage fees
* Provide secure REST API access
* Implement role-based authorization

---

## ✨ Features

### Authentication & Authorization

* JWT authentication
* Access and refresh tokens
* Custom User model
* Admin, Faculty and Student roles
* Django Groups
* Initial API permission system

### Academic Management

* Departments
* Students
* Faculty
* Courses
* Enrollments
* Classrooms
* Timetable
* Exams
* Grades / Results

### Administration

* Fees management
* Notifications
* Django Admin interface
* PostgreSQL database

### REST API

* CRUD operations
* Filtering
* Searching
* Ordering
* JWT-protected endpoints
* API validation

---

## 🛠️ Tech Stack

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Programming language |
| Django                | Backend framework    |
| Django REST Framework | REST API             |
| PostgreSQL            | Database             |
| Simple JWT            | Authentication       |
| django-filter         | Filtering            |
| drf-yasg              | API documentation    |
| Django Admin          | Administration       |
| Git / GitHub          | Version control      |

---

## 🏗️ Architecture

```text
                    Client
                      │
                      ▼
              Django REST API
                      │
          ┌───────────┴───────────┐
          │                       │
       JWT Auth              REST Endpoints
          │                       │
          └───────────┬───────────┘
                      │
                Django Models
                      │
                      ▼
                  PostgreSQL
```

---

## 📂 Project Structure

```text
college_erp/
│
├── accounts/
├── students/
├── faculty/
├── departments/
├── courses/
├── enrollments/
├── attendance/
├── classrooms/
├── timetable/
├── exams/
├── results/
├── fees/
├── notifications/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🗄️ Data Model

The main entities are:

```text
Department
    │
    ├── Students
    ├── Faculty
    └── Courses
            │
            ├── Enrollments
            ├── Exams
            └── Timetable

Student
    ├── Attendance
    ├── Enrollments
    ├── Results
    └── Fees

Faculty
    ├── Courses
    ├── Attendance
    └── Exams
```

---

## 🔐 Authentication

The API uses **JWT authentication**.

### Obtain tokens

```http
POST /api/token/
```

Request:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Response:

```json
{
    "refresh": "YOUR_REFRESH_TOKEN",
    "access": "YOUR_ACCESS_TOKEN"
}
```

### Authenticate API requests

Include the access token in the request header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Refresh token

```http
POST /api/token/refresh/
```

---

## 👥 Roles & Permissions

The application supports three main roles:

| Role    | Description                           |
| ------- | ------------------------------------- |
| Admin   | Full system management                |
| Faculty | Academic management                   |
| Student | Access to student-related information |

Initial role-based API permissions are implemented using Django Groups and Django REST Framework permissions.

> More granular object-level permissions are planned as a future improvement.

---

## 🔌 API Endpoints

### Authentication

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/token/`         | Obtain JWT tokens    |
| POST   | `/api/token/refresh/` | Refresh access token |

### Students

| Method | Endpoint              | Description              |
| ------ | --------------------- | ------------------------ |
| GET    | `/api/students/`      | List students            |
| POST   | `/api/students/`      | Create student           |
| GET    | `/api/students/{id}/` | Get student              |
| PUT    | `/api/students/{id}/` | Update student           |
| PATCH  | `/api/students/{id}/` | Partially update student |
| DELETE | `/api/students/{id}/` | Delete student           |

### Other API modules

```text
/api/faculty/
/api/departments/
/api/courses/
/api/enrollments/
/api/attendance/
/api/classrooms/
/api/timetable/
/api/exams/
/api/results/
/api/fees/
/api/notifications/
```

> Endpoint availability will expand as additional ViewSets and permissions are implemented.

---

## 🔎 Filtering, Searching & Ordering

Example:

```http
GET /api/students/?department=1
```

Search:

```http
GET /api/students/?search=john
```

Ordering:

```http
GET /api/students/?ordering=student_id
```

---

## 📖 API Documentation

Interactive API documentation is provided using Swagger/OpenAPI.

Once enabled, documentation will be available at:

```text
/api/docs/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd college_erp
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=college_erp
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create an administrator

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Testing

Run Django system checks:

```bash
python manage.py check
```

Run tests:

```bash
python manage.py test
```

---

## 🖥️ Django Admin

The Django Admin interface provides management of:

* Users
* Students
* Faculty
* Departments
* Courses
* Enrollments
* Attendance
* Timetable
* Exams
* Results
* Fees
* Notifications

Admin URL:

```text
/admin/
```

---

## 🚀 Deployment

The project is designed to be deployed as a production Django REST API with PostgreSQL.

### Production architecture

```text
Frontend
   │
   ▼
Django REST API
   │
   ▼
PostgreSQL
```

Deployment configuration includes:

* Production environment variables
* PostgreSQL
* Static files
* CORS configuration
* Production `DEBUG=False`
* Secure Django settings

> Deployment details and live API URL will be added after the production deployment is completed.

---

## 📸 Screenshots

### Django Admin

*Add screenshot here*

### Swagger API

*Add screenshot here*

### JWT Authentication

*Add screenshot here*

---

## 🗺️ Roadmap

### Completed

* [x] Django project setup
* [x] PostgreSQL integration
* [x] Custom User model
* [x] Student management
* [x] Faculty management
* [x] Departments
* [x] Courses
* [x] Enrollments
* [x] Attendance
* [x] Classrooms
* [x] Timetable
* [x] Exams
* [x] Results
* [x] Fees
* [x] Notifications
* [x] Django Admin
* [x] Django REST Framework
* [x] JWT authentication
* [x] Filtering/searching/ordering
* [x] Initial role-based permissions

### Planned

* [ ] Complete role-based permissions
* [ ] Object-level permissions
* [ ] Complete API coverage for all models
* [ ] Automated tests
* [ ] Swagger/OpenAPI improvements
* [ ] Production deployment
* [ ] React frontend
* [ ] Docker
* [ ] CI/CD

---

## 🔮 Future Improvements

Possible future improvements include:

* React frontend
* Docker containerization
* CI/CD pipeline
* Advanced role-based access control
* Email notifications
* File/document management
* Advanced reporting
* Automated testing
* Production monitoring

---

## 📄 License

This project is currently intended as a portfolio and educational project.

---

## 👨‍💻 Author

**Your Name**

GitHub: `https://www.github.com/dmitruz`

LinkedIn: `https://www.linkedin.com/in/dmytro-ruzhytskyi/`
