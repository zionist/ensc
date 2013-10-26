#!/usr/bin/env python
import os
import sys
from eventlet import wsgi
import eventlet

sys.path.append("/home/slaviann/work/ensc")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ensc.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


wsgi.server(eventlet.listen(('0.0.0.0', 8080)), application)
