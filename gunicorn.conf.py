workers = 4  # Number of Gunicorn worker processes
bind = '0.0.0.0:8000'  # IP address and port to bind Gunicorn to
timeout = 120  # Timeout for requests in seconds
loglevel = 'info'  # Logging level

# Set the path to your Django project's WSGI application
app_name = 'hitcoin'  # Replace with your project name
application = f'{app_name}.wsgi:application'
