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

In case you are using South, you can alternatively do:

.. code-block::  shell

    python manage.py migrate gipsy_toolbar
    
    
Setup your menu items in the admin.

And finaly, install the toolbar in your templates with a template tag:

.. code-block::  html

    {% load gipsy_toolbar %}
    
    {% gipsy_toolbar %}

For the admin part, you will need to overwrite templates with the same code as above: {templates}/admin/base.html 

If you are using a cache engine such as Varnish, you can use a bundled middleware in order to set a cookie that you can use to deactivate cache to display the toolkbar for staff admins. Happy to hear abotu a cleaner solution.

.. code-block::  python

    MIDDLEWARE_CLASSES = (
        ...
        'gipsy_toolbar.middleware.GipsyToolbarMiddleware',
        ...
    )

Please feel free to contribute.
