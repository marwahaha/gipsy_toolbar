#############
Gipsy toolbar
#############

This Django app manages a toolbar for admins with shortcuts to easily navigate to most relevant admin features.

*******
Install
*******

It is strongly recommanded to install this theme from GIT with PIP onto you project virtualenv.

Add this line to your requirements.txt file:

.. code-block::  shell-session

    -e git+https://github.com/RevSquare/gipsy_toolbar#egg=gipsy_toolbar

And run:

.. code-block::  shell-session

    pip install -r requirements.txt

*****
Setup
*****

Simply add the app in your installed apps list in settings.py

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'gipsy_toolbar'
        ...
    )

Then install your model with 

.. code-block::  shell

    python manage.py syncdb
    
    
Setup your menu items in the admin.

And finaly, install the toolbar in your templates with a template tag:

.. code-block::  html

    {% load gipsy_toolbar %}
    
    {% gipsy_toolbar %}

Please feel free to contribute.
