Requirements :
1. Django (pip install django)
2. Django rest Framework (pip install djangorestframework)

steps to run the project :
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py fakedata (populating database)
4. python manage.py fakedatawithemail (populating database)
5. python manage.py unauthfakedata (populating database)
6. python manage.py runserver

working of APIs :
1. search API - used for searching an object by given name or number. If not given then all objects.
2. spam API - used for marking the number as spam
3. create API - used for creating an user
4. contact list API - used for creating unregistered users which will be coming from contact list passed by registered user

Postman link for APIs testing :
https://www.getpostman.com/collections/8dcce57c82930d16827e




