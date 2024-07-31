Setup Instructions
Prerequisites
    INSTALL REDIS
        sudo snap install redis
    Python 3.8+: Ensure Python is installed.
    pip: Python package installer.

1. Clone the Repository
   Clone the repository to your local machine:
   git clone git@github.com:kuldeep203/openai_image_gen.git
   cd blog
2. Create and Activate a Virtual Environment
   python -m venv venv
3. Create a .env file in the root of your project with the following variables:
    OPENAI_KEY=''
4. Active venv
   source venv/bin/activate
5. Install Dependencies
   pip install -r requirements.txt
6. Database Setup
   python3 manage.py makemigrations
   python3 manage.py migrate
7. Create a superuser to access the Django admin interface
   python manage.py createsuperuser
8. python manage.py runserver
9. API Documentation
   Interactive API documentation is available at:

   Swagger UI: http://127.0.0.1:8000/swagger/

10. Authentication
   JWT Authentication
   Obtain Access and Refresh Tokens:

          Endpoint: /api/token/
          Method: POST
          Body:
          {
          "username": "your_username",
          "password": "your_password"
          }
11. Refresh Access Token:

           Endpoint: /api/token/refresh/
           Method: POST
           Body:

          {
          "refresh": "your_refresh_token"
          }

Include the JWT token in the Authorization header for authenticated requests:

Authorization: Bearer <your-access-token>

12. CSRF Token
    For POST requests, include the CSRF token in the request headers. Retrieve the CSRF token by making a GET request to
    any endpoint with CSRF protection enabled.


13. Start Celery Worker
In a separate terminal, activate your virtual environment and run:

bash
Copy code
celery -A image_gen_project worker --loglevel=info

