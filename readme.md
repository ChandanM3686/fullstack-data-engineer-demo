# Tracker Demo – Full Stack Data Engineer Task

A simple Django web application using REST APIs and a PostgreSQL-ready configuration, featuring:

- Basic CRUD APIs for User and Activity entities
- Integration with a third-party API (OpenWeather)
- A clean structure that can be easily extended with data visualization or reporting features

This project was built as part of the Full Stack Data Engineer demo task.

---

## Tech Stack

- Python 3.11+
- Django 5.x
- Django REST Framework
- SQLite (default for local development)
- PostgreSQL / Supabase (production-ready configuration)
- Requests (for external API calls)

---

## Features

### CRUD REST APIs
- **User**
  - Fields: `name`, `email`
- **Activity**
  - Fields: `user`, `activity_name`, `created_at`
  - Each activity is linked to a user

### Third-Party API Integration
- `/api/weather/?city=CityName`
- Fetches live weather data from the OpenWeather API and returns JSON response

### Admin Interface
- Users and Activities are registered in Django Admin
- Allows quick inspection and manual data entry

> Note: Data visualization or reporting can be added either via aggregated API endpoints
> (e.g. activity counts per day) or a simple frontend using charts.
> The project structure is designed to make this extension straightforward.

---

## Project Structure

```text
demo_project/
├── demo_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tracker/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── tests.py
│   └── migrations/
├── manage.py
└── README.md
