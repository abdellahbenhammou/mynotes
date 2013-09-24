"""
WSGI config for myNotes project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
#import os
#import sys

#sys.path.append("/var/www/mynotes/ ")
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "myNotes.settings"
#os.environ["DJANGO_SETTINGS_MODULE"] = 'myNotes.settings'

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
#import django.core.handlers.wsgi
#from django.core.wsgi import get_wsgi_application

#application = django.core.handlers.wsgi.WSGIHandler()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
import os 
import sys
 
# this line is added so python is aware of the application
# this is absolute path to the app.
sys.path.append('/var/www/mynotes/myNotes')
 
# this is simply a check to see if the site is in syspath as well this is one directory up from application
path = '/var/www/mynotes'
if path not in sys.path:
    sys.path.insert(0,'/var/www/mynotes')
 
# this is the settings file needed to start django with.
os.environ['DJANGO_SETTINGS_MODULE'] = 'myNotes.settings'
 
# import handler and activate application
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

