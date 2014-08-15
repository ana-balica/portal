Installing Systers Portal
=========================

#. Make sure you have installed Python 2.6.5 or higher, pip and virtualenv
#. Create a virtual environment and install dependencies::

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements-dev.txt

#. Make sure you have PostgreSQL database up and running
#. Create systersdb database, where systersdb might be any suitable name
#. Fill in the database details in ``systers_portal/settings/dev.py``
#. Run export ``SECRET_KEY=foobarbaz`` in your terminal, ideally the secret key
   should be 40 characters long, unique and unpredictable
#. Run python ``systers_portal/manage.py syncdb``
#. Run python ``systers_portal/manage.py runserver`` to start the development
   server. When in testing or production, feed the respective settings file from
   the command line, e.g. for testing
   ``python manage.py runserver --settings=systers_portal.settings.testing``
#. Before commiting run ``flake8 systers_portal`` and fix PEP8 warnings
#. Run python
   ``systers_portal/manage.py test --settings=systers_portal.settings.testing``
   to run all the tests