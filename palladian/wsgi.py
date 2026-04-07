import os
import sys
from django.core.wsgi import get_wsgi_application

# Ensure the root project directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'palladian.settings')

application = get_wsgi_application()
app = application
