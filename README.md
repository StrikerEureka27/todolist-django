
# Project setup
(Python + Django)

First of all, we have to establish a virtual enviroment to isolate our project under specific packages. 

**Create a virtual enviroment**

```
virtualenv venv
```

**Activate environment**

```
    source venv/bin/activate
```

**Install Django pip dependency**

```
python -m pip install Django
```

**Create a new django project**

```
django-admin startproject <name> .
```

> Use dot **( . )** if we want to create to project in the same root directory

Starting a django server 

```
python manage.py runserver
```

**Then to create a new app we can use**

```
python manage.py startapp <name>
```

To add the app to the main project we have to add app name to INSTALLED_APP list on `<project_name>/settings.py`

---

## Migrations

**Then to migrate the already included apps we execute**
```
python manage.py migrate
```

## Django REST framework 

**Install pip dependency**
```
pip install djangorestframework
```
	
To work in the future with both frontend and backend side, in developing stage we migth use a cors headers library to allow traffic between servers.

```
pip install django-cors-headers
```

> Don’t forget to added to INSTALLED_APPS list

We have to add cors headers app to MIDDLEWARS list

If we create / delete  or update a model we have to perfom the next command to preparte migration to a project

```
Python manage.py makemigrations <app name> (<app name> 
```

> It's optional if we want only migrate a especif app model)

Then we have to execute this command to finish the workflow

```
python manage.py migrate <app name>
```
## Setup superuser

```
python manage.py createsuperuser <user_name>
```

To manage from admin panel models, we have to add model to admin.py file

```
admin.site.register(<app name>)
```
