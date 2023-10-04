web: python manage.py runserver
beat: celery -A celery_project beat -l info
worker: celery -A celery_project.celery worker --pool=solo -l info
