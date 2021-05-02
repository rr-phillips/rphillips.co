import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return [response.encode()]


# breaks it
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rphillips.settings')

# application = get_wsgi_application()

# didn't work
# import rephillips.wsgi
# application = rephillips.wsgi.application

# from rphillips.wsgi import RPhillipsApplication
# application = RPhillipsApplication(application)