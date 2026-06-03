# portfolio-combined
# Shaun Benny — Full Stack Developer Portfolio

A dynamic, full-stack portfolio website built with Python and Django. This project features a public-facing portfolio, a custom-built secure Admin Dashboard for managing content (Projects, Skills, Contact Messages), and a fully documented REST API.

##  Features

* **Dynamic Content Management:** Add, edit, and delete Projects and Skills via a custom Admin Dashboard.
* **Currently running on sqllite and will upgrade to postgres sql in proper ipadresss server 
* **REST API:** Built with Django REST Framework (DRF) to serve portfolio data.
* **Interactive API Docs:** Auto-generated OpenAPI 3.0 documentation using Swagger UI (`drf-spectacular`)but currently there is no drf views so api wontbe visible to test in swagger.
* **Production Ready:** Configured with WhiteNoise for static file serving, Gunicorn for the application server, and  database integration.
* **Environment Security:** Secured using `python-dotenv` to manage secret keys and debug states.

##  Tech Stack

* **Backend:** Python 3.13+, Django 6.x, Django REST Framework
* **Database:** SQLite (Local Development) / SQLlite(temporary) (Production)
* **API Documentation:** drf-spectacular (Swagger)
* **Deployment:** Render (PaaS), Gunicorn, WhiteNoise

---

## 💻 Local Development Setup

Follow these instructions to set up the project on your local machine (macOS/Linux).

### 1. Clone the Repository
```bash
git clone [https://github.com/shaunbenny24/portfolio-combined.git](https://github.com/shaunbenny24/portfolio-combined.git)
cd portfolio-combined