# Employee Management System API

A Django-based RESTful API for managing employees, departments, attendance, and performance. Includes authentication, Swagger documentation, and interactive data visualizations with Chart.js.

## Features

✅ Token Authentication  
✅ Modular Django App Structure  
✅ PostgreSQL Database (Dockerized)  
✅ REST API with CRUD operations  
✅ Swagger & Redoc Docs  
✅ Chart.js Visualizations  
✅ Data Seeding with Faker  
✅ Pagination, Filtering, Searching  
✅ Docker Support

## Tech Stack

- Python
- Django & Django REST Framework
- PostgreSQL
- Docker + docker-compose
- Chart.js (for frontend charts)
- drf-yasg (Swagger docs)
- Faker (for test data)

## Project Structure

# Employee Management System API

A Django-based RESTful API for managing employees, departments, attendance, and performance. Includes authentication, Swagger documentation, and interactive data visualizations with Chart.js.

---

## ✅ Features

- Token Authentication  
- Modular Django App Structure  
- PostgreSQL Database (Dockerized)  
- REST API with CRUD operations  
- Swagger & Redoc Docs  
- Chart.js Visualizations  
- Data Seeding with Faker  
- Pagination, Filtering, Searching  
- Docker Support  

---

## 🛠 Tech Stack

- Python
- Django & Django REST Framework
- PostgreSQL
- Docker + docker-compose
- Chart.js (for frontend charts)
- drf-yasg (Swagger docs)
- Faker (for test data)

---

## 🗂 Project Structure

```plaintext
employee_project/
├── .env
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── project_structure.txt
├── requirements.txt
├── render.yaml # Deployment configuration file for Render.com
├── README.md
├── attendance/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── departments/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── employees/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── management/commands/seed_data.py
│   └── migrations/
├── performance/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── employee_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates/
    ├── charts.html
    

        



## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Shelby700/employee_project.git
cd employee_project

2. Setup Environment Variables
Create a .env file from the provided .env.example:

cp .env.example .env
Edit .env to match your database credentials, e.g.:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=emsdb
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432

3. Build with Docker
docker-compose up --build

4. Run Migrations & Seed Data
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py seed_data

5. Access the App
Swagger: http://localhost:8000/swagger/

Redoc: http://localhost:8000/redoc/

Charts: http://localhost:8000/charts/

API Authentication
Use DRF Token Authentication:

1. Get Token
POST /api-token-auth/
{
  "username": "your_username",
  "password": "your_password" 
}
Response:

{"token": "your_token_here"}
2. Use in Requests
Include the token in headers:

Authorization: Token your_token_here
Chart Pages
Employees per Department (Pie Chart)

Monthly Attendance Overview (Bar Chart)

These are rendered using Chart.js in the charts.html template.

Useful Commands
# Run tests
docker-compose exec web python manage.py test

# Seed random data
docker-compose exec web python manage.py seed_data

# Create a new app
docker-compose exec web python manage.py startapp employee_project
