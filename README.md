# School Management System

A comprehensive web application for managing various aspects of a school, including student information, library records, fee management, and user roles. This system allows administrators, office staff, and librarians to efficiently manage their respective tasks through role-based access.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)

## Features

- **Role-Based Access Control (RBAC)**: Separate roles for Admin, Office Staff, and Librarians.
- **Student Management**: CRUD operations for student records with fields like first name, last name, student ID, email, phone, date of birth, address, emergency contact, grade, and section.
- **Library Management**: Track library history and manage student borrowing records.
- **Fee Management**: Maintain records of student fees with the ability to add, edit, and view payment history.
- **Dashboard**: Admin dashboard with views for student details, library records, and fee records.
- **User Authentication**: Secure login with the Django authentication system.
  
## Technologies Used

- **Backend**: Django (Python) and PostgreSQL
- **Frontend**: HTML, CSS (Bootstrap for styling), and JavaScript

## Getting Started

These instructions will help you set up a local development environment to run the School Management System on your machine.

### Prerequisites

- Python 3.x
- PostgreSQL
- Virtual Environment (recommended)
- Git

### Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/JishnuRameshC/school-management-system.git
    cd schoolmanagement
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure PostgreSQL:**
   - Create a new PostgreSQL database and user.
   - Update the `DATABASES` settings in `settings.py` with your database credentials.

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser for admin access:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the application:**
   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

- **Admin**: Access the full dashboard to manage students, library records, fees, and user roles.
- **Office Staff**: Restricted access to student and fee records.
- **Librarian**: Restricted access to library records.
- **Authentication**: Login required for all roles to access specific functionalities.

### User Roles and Permissions

| Role         | Permissions                             |
|--------------|----------------------------------------|
| Admin        | Full access to all features            |
| Office Staff | Access to student and fee records only |
| Librarian    | Access to library records only         |


