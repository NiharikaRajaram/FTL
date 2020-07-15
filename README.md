# FTL
FTL


1.  Django
$ pip install django

2. Start a new Django Project
$ django-admin startproject mysite

3. Run the Django server
$ python manage.py runserver

4. Create a new app for our API
$ python manage.py startapp myapi

5. Edit mysite/settings.py and add this
INSTALLED_APPS = [
    'myapi.apps.MyapiConfig',
    ... # Leave all the other INSTALLED_APPS
]

6. Migrate the database
$ python manage.py migrate

7. Make models in models.py

8. Make migrations
$ python manage.py makemigrations
$ python manage.py migrate

9. Register the model with the admin site ie., myapi/admin.py

10. Run server and add instances of models

11. Install Djangorestframework and make changes in mysite/settings.py
$ pip install djangorestframework

INSTALLED_APPS = [
    # All your installed apps stay the same
    ...
    'rest_framework',
]

12. Serialize the data in myapi/serialize.py

13. Render data in JSON format in view.py
