"""
WSGI config for Ehousing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


try:
    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ehousing.settings')

    application = get_wsgi_application()
except Exception as e:
    print("Error importing WSGI application:", e)
   
