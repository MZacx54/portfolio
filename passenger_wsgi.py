import os
import sys

# Define path to the application
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Import the Passenger WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
