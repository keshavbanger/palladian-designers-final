import os
import sys
from django.core.wsgi import get_wsgi_application

# Ensure the root project directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'palladiun.settings')

# This is the main application handler
application = get_wsgi_application()

# WhiteNoise bypass for Vercel
try:
    from whitenoise import WhiteNoise
    from django.conf import settings
    application = WhiteNoise(application, root=settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)
except ImportError:
    pass

# Aliases for Vercel and other platforms
app = application
handler = application
