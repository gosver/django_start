import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "z_config.settings")
application = get_wsgi_application()
execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8001'])
