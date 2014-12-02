GAE_Django14
============

Testing Django 1.4 on GAE using Python 2.7 and MySQL

This uploads to my own project on Google App Engine.

##Explicitly Pip Installed:

- Django (1.4)
- google-api-python-client (1.3.1)
- MySQL-python (1.2.5)
- oauth2client (1.4.2)
- python-gflags (2.0)
- simplejson (3.6.5)


##Things to remember:

Add google appengine to python path and run syncdb on production databases.

```
export PYTHONPATH="$PYTHONPATH:/home/user/google_appengine:/home/user/google_appengine/lib/django_1_3"
```
```
SETTINGS_MODE='prod' ./manage.py syncdb
```

##Handy Links:

- [Google Cloud SQL - Django Support](https://cloud.google.com/appengine/docs/python/cloud-sql/django)
- [Third-Party Libraries in Python 2.7](https://cloud.google.com/appengine/docs/python/tools/libraries27)
- [Django 1.4 Documentation](https://docs.djangoproject.com/en/1.4/)
- [Using Templates (Jinja)](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/templates)
- [Jinja Documentation](http://jinja.pocoo.org/docs/dev/)