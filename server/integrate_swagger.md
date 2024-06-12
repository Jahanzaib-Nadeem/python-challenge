Here's a step by step explanation for each step I took in integrating Swagger with the Django project.

### 1. Install Django Rest Swagger library
Installed the Django Rest Swagger library to our project. This library provides tools to generate a Swagger UI for Django REST API. It’s installed via pip, Python’s package installer.

### 2. Added in INSTALLED_APPS in settings.py
After installation, the Django Rest Swagger application needs to be registered within the Django project. This is done by adding 'drf_yasg' to the `INSTALLED_APPS` list in our project’s `settings.py` file. This registration tells Django to include the Swagger UI in the project’s setup, enabling it to generate and display the API documentation.

### 3. Setup Django Rest Swagger in settings.py
Further configuration of Django Rest Swagger is required in the `settings.py` to customize how the Swagger documentation behaves. This could include settings like the depth of documentation, the format of the API endpoints, and authentication methods used when accessing the Swagger documentation.

### 4. Define routes to access swagger through django
Routes (URL paths) that lead to the Swagger documentation UI need to be defined in your project's URL configuration. These routes dictate where and how the Swagger UI can be accessed within your application, allowing users and developers to view the API documentation through specific URLs.

### 5. Define schema view to access swagger through django
A schema view is set up to serve the actual Swagger documentation. To allow detailed documentation of the API, I manually defined a schema view.

### 6. Access swagger through browser
With the routes and schema view defined, the Swagger documentation can now be accessed via a web browser. Users can navigate to the URL (localhost:8000/swagger) to view and interact with the API documentation. This interactive documentation allows users to see the available endpoints, try out API calls directly from the browser, and view example responses.
