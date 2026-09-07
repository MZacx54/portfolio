import os
import sys
import traceback

# Define path to the application
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception:
    error_msg = traceback.format_exc()
    def application(environ, start_response):
        status = '200 OK'
        body = f"<h2>WSGI Startup Error</h2><pre style='background:#f8d7da;color:#721c24;padding:15px;border:1px solid #f5c6cb;font-size:14px;'>{error_msg}</pre>".encode('utf-8')
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
            ('Content-Length', str(len(body)))
        ]
        start_response(status, response_headers)
        return [body]
