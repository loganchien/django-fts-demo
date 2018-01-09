Django PostgreSQL Full-text Search Demo App
===========================================

This is the full-text search demo app for Django and PostgreSQL.

Read [my blog post](https://logan.tw/posts/2017/12/30/full-text-search-with-django-and-postgresql/) for more details.


## Installation

To run this demo app, `python3` and `postgresql` are required.  In Ubuntu
17.04, these can be installed with:

```
sudo apt-get install python3 postgresql
```

In addition, the python packages specified in `requirements.txt` are required
as well.  These python packages can be installed with:

```
pip install -r requirements.txt
```


## Settings

Open `fts_demo/settings.py` and change the database settings:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '[db_name]',
        'USER': '[username]',
        'PASSWORD': '[password]',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
